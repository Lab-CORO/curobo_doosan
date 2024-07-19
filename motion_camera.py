#
# Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.
#

# Standard Library

# Third Party
import cv2
import numpy as np
import torch
from matplotlib import cm
from nvblox_torch.datasets.realsense_dataset import RealsenseDataloader

# CuRobo
from curobo.geom.sdf.world import CollisionCheckerType
from curobo.geom.types import Cuboid, WorldConfig
from curobo.types.base import TensorDeviceType
from curobo.types.camera import CameraObservation
from curobo.types.math import Pose
from curobo.types.robot import JointState, RobotConfig
from curobo.types.state import JointState
from curobo.util_file import get_robot_configs_path, get_world_configs_path, join_path, load_yaml
from curobo.wrap.model.robot_world import RobotWorld, RobotWorldConfig
from curobo.wrap.reacher.motion_gen import MotionGen, MotionGenConfig, MotionGenPlanConfig

import argparse


def demo_motion_gen(js=False):
    # Standard Library
    # PLOT = True
    radius = 0.05
    act_distance = 0.4
    voxel_size = 0.05
    render_voxel_size = 0.02
    clipping_distance = 0.7
    tensor_args = TensorDeviceType()

    collision_checker_type = CollisionCheckerType.BLOX
    world_cfg = WorldConfig.from_dict(
        {
            "blox": {
                "world": {
                    "pose": [0, 0, 0, 1, 0, 0, 0],
                    "integrator_type": "occupancy",
                    "voxel_size": 0.02,
                }
            }
        }
    )
    tensor_args = TensorDeviceType()

    robot_cfg = load_yaml(join_path(get_robot_configs_path(), "franka.yml"))["robot_cfg"]

    j_names = robot_cfg["kinematics"]["cspace"]["joint_names"]
    default_config = robot_cfg["kinematics"]["cspace"]["retract_config"]

    # robot, _ = add_robot_to_scene(robot_cfg, my_world, "/World/world_robot/")

    world_cfg_table = WorldConfig.from_dict(
        load_yaml(join_path(get_world_configs_path(), "collision_wall.yml"))
    )

    world_cfg_table.cuboid[0].pose[2] -= 0.01
    world_cfg.add_obstacle(world_cfg_table.cuboid[0])
    world_cfg.add_obstacle(world_cfg_table.cuboid[1])



    # robot_file = "franka.yml"
    motion_gen_config = MotionGenConfig.load_from_robot_config(
        robot_cfg,
        world_cfg,
        tensor_args,
        trajopt_tsteps=32,
        collision_checker_type=CollisionCheckerType.BLOX,
        use_cuda_graph=True,
        num_trajopt_seeds=12,
        num_graph_seeds=12,
        interpolation_dt=0.03,
        collision_activation_distance=0.025,
        acceleration_scale=1.0,
        self_collision_check=True,
        maximum_trajectory_dt=0.25,
        finetune_dt_scale=1.05,
        fixed_iters_trajopt=True,
        finetune_trajopt_iters=300,
        minimize_jerk=True,
    )

    motion_gen = MotionGen(motion_gen_config)
    print("warming up..")
    motion_gen.warmup()

    world_model = motion_gen.world_collision
    realsense_data = RealsenseDataloader(clipping_distance_m=clipping_distance)
    data = realsense_data.get_data()

    camera_pose = Pose.from_list([0, 0, 0, 0.707, 0.707, 0, 0])


    data_camera = CameraObservation(  # rgb_image = data["rgba_nvblox"],
        depth_image=data["depth"], intrinsics=data["intrinsics"], pose=camera_pose
    )
    data_camera = data_camera.to(device=tensor_args.device)
    world_model.add_camera_frame(data_camera, "world")
    world_model.process_camera_frames("world", False)
    torch.cuda.synchronize()
    world_model.update_blox_hashes()

    bounding = Cuboid("t", dims=[1, 1, 1.0], pose=[0, 0, 0, 1, 0, 0, 0])
    voxels = world_model.get_voxels_in_bounding_box(bounding, voxel_size)
    if voxels.shape[0] > 0:
        voxels = voxels[voxels[:, 2] > voxel_size]
        voxels = voxels[voxels[:, 0] > 0.0]
       
        voxels = voxels.cpu().numpy()
        voxel_viewer.update_voxels(voxels[:, :3])

        voxel_viewer.update_voxels(voxels[:, :3])

    # draw_points(voxels)

    if True:
        depth_image = data["raw_depth"]
        color_image = data["raw_rgb"]
        depth_colormap = cv2.applyColorMap(
            cv2.convertScaleAbs(depth_image, alpha=100), cv2.COLORMAP_VIRIDIS
        )
        color_image = cv2.flip(color_image, 1)
        depth_colormap = cv2.flip(depth_colormap, 1)

        images = np.hstack((color_image, depth_colormap))

        cv2.namedWindow("NVBLOX Example", cv2.WINDOW_NORMAL)
        cv2.imshow("NVBLOX Example", images)
        key = cv2.waitKey(1)
        # Press esc or 'q' to close the image window
        if key & 0xFF == ord("q") or key == 27:
            cv2.destroyAllWindows()
            



    # motion_gen.warmup(enable_graph=True, warmup_js_trajopt=js, parallel_finetune=True)
    # robot_cfg = load_yaml(join_path(get_robot_configs_path(), robot_file))["robot_cfg"]
    # robot_cfg = RobotConfig.from_dict(robot_cfg, tensor_args)
    retract_cfg = motion_gen.get_retract_config()
    state = motion_gen.rollout_fn.compute_kinematics(
        JointState.from_position(retract_cfg.view(1, -1))
    )

    retract_pose = Pose(state.ee_pos_seq.squeeze(), quaternion=state.ee_quat_seq.squeeze())
    start_state = JointState.from_position(retract_cfg.view(1, -1))
    goal_state = start_state.clone()

    start_state.position[0, 0] += 0.25
    # goal_state.position[0,0] += 0.5
    if js:
        result = motion_gen.plan_single_js(
            start_state,
            goal_state,
            MotionGenPlanConfig(max_attempts=1, time_dilation_factor=0.5),
        )
    else:
        result = motion_gen.plan_single(
            start_state,
            retract_pose,
            MotionGenPlanConfig(
                max_attempts=1,
                timeout=5,
                time_dilation_factor=0.5,
            ),
        )
        new_result = result.clone()
        new_result.retime_trajectory(0.5, create_interpolation_buffer=True)
        print(new_result.optimized_dt, new_result.motion_time, result.motion_time)
    print(
        "Trajectory Generated: ",
        result.success,
        result.solve_time,
        result.status,
        result.optimized_dt,
    )

if __name__ == "__main__":
    # setup_curobo_logger("error")
    demo_motion_gen(js=False)

