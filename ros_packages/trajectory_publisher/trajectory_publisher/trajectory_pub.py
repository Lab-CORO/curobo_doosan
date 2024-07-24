#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from moveit_msgs.msg import DisplayTrajectory
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from std_msgs.msg import Header
import torch
from curobo.geom.sdf.world import CollisionCheckerType
from curobo.geom.types import Cuboid, WorldConfig
from curobo.types.base import TensorDeviceType
from curobo.types.camera import CameraObservation
from curobo.types.math import Pose
from curobo.types.robot import JointState, RobotConfig
from curobo.util_file import get_robot_configs_path, get_world_configs_path, join_path, load_yaml
from curobo.wrap.model.robot_world import RobotWorld, RobotWorldConfig
from curobo.wrap.reacher.motion_gen import MotionGen, MotionGenConfig, MotionGenPlanConfig
from nvblox_torch.datasets.realsense_dataset import RealsenseDataloader

class TrajectoryPublisher(Node):
    def __init__(self):
        super().__init__('trajectory_publisher')
        self.publisher_ = self.create_publisher(DisplayTrajectory, 'display_trajectory', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)  # Publie toutes les secondes
        self.initialize_trajectory()

    def initialize_trajectory(self):
        # Initialiser la configuration et générer la trajectoire
        self.setup_trajectory()

    def setup_trajectory(self):
        # Initialiser les configurations et le générateur de trajectoire
        self.radius = 0.05
        self.act_distance = 0.4
        self.voxel_size = 0.05
        self.render_voxel_size = 0.02
        self.clipping_distance = 0.7
        self.tensor_args = TensorDeviceType()

        self.collision_checker_type = CollisionCheckerType.BLOX

        self.world_cfg = WorldConfig.from_dict(
            {
                "blox": {
                    "world": {
                        "pose": [0, 0, 0, 1, 0, 0, 0],
                        "integrator_type": "occupancy",
                        "voxel_size": 0.02,
                    },
                },
                "mesh": {
                    "base_scene": {
                        "pose": [10.5, 0.080, 1.6, 0.043, -0.471, 0.284, 0.834],
                        "file_path": "scene/nvblox/srl_ur10_bins.obj",
                    },
                },
                "cuboid": {
                    "table": {
                        "dims": [5.0, 5.0, 0.2],  # x, y, z
                        "pose": [0.0, 0.0, -0.1, 1, 0, 0, 0.0],  # x, y, z, qw, qx, qy, qz
                    },
                },
            }
        )

        self.robot_cfg = load_yaml(join_path(get_robot_configs_path(), "/pkgs/curobo_doosan/src/m1013/m1013.yml"))["robot_cfg"]
        self.motion_gen_config = MotionGenConfig.load_from_robot_config(
            self.robot_cfg,
            self.world_cfg,
            self.tensor_args,
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

        self.motion_gen = MotionGen(self.motion_gen_config)
        self.motion_gen.warmup()

        self.world_model = self.motion_gen.world_collision
        realsense_data = RealsenseDataloader(clipping_distance_m=self.clipping_distance)
        data = realsense_data.get_data()
        camera_pose = Pose.from_list([0, 0, 0, 0.707, 0.707, 0, 0])
        data_camera = CameraObservation(depth_image=data["depth"], intrinsics=data["intrinsics"], pose=camera_pose)
        data_camera = data_camera.to(device=self.tensor_args.device)
        self.world_model.add_camera_frame(data_camera, "world")
        self.world_model.process_camera_frames("world", False)
        torch.cuda.synchronize()
        self.world_model.update_blox_hashes()

        bounding = Cuboid("t", dims=[1, 1, 1.0], pose=[0, 0, 0, 1, 0, 0, 0])
        voxels = self.world_model.get_voxels_in_bounding_box(bounding, self.voxel_size)
        if voxels.shape[0] > 0:
            voxels = voxels[voxels[:, 2] > self.voxel_size]
            voxels = voxels[voxels[:, 0] > 0.0]
            voxels = voxels.cpu().numpy()

        retract_cfg = self.motion_gen.get_retract_config()
        state = self.motion_gen.rollout_fn.compute_kinematics(JointState.from_position(retract_cfg.view(1, -1)))
        retract_pose = Pose(state.ee_pos_seq.squeeze(), quaternion=state.ee_quat_seq.squeeze())
        start_state = JointState.from_position(retract_cfg.view(1, -1))
        goal_pose = Pose.from_list([-0.4, 0.0, 0.4, 1.0, 0.0, 0.0, 0.0])

        start_state.position[0, 0] += 0.25

        result = self.motion_gen.plan_single(
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
        self.traj = result.get_interpolated_plan()

    def timer_callback(self):
        # Créer un message DisplayTrajectory
        msg = DisplayTrajectory()
        msg.header = Header(stamp=self.get_clock().now().to_msg(), frame_id='base_link')
        msg.trajectory = [self.convert_to_joint_trajectory(self.traj)]
        msg.trajectory_start = self.get_trajectory_start()

        # Publier le message
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing trajectory')

    def convert_to_joint_trajectory(self, traj):
        # Convertir la trajectoire en JointTrajectory
        trajectory = JointTrajectory()
        trajectory.joint_names = ['joint1', 'joint2', 'joint3']  # Nommer vos joints ici

        for point in traj:
            traj_point = JointTrajectoryPoint()
            traj_point.positions = point.positions.tolist()
            traj_point.time_from_start.sec = int(point.time_from_start)
            traj_point.time_from_start.nanosec = int((point.time_from_start - int(point.time_from_start)) * 1e9)
            trajectory.points.append(traj_point)

        return trajectory

    def get_trajectory_start(self):
        # Créer un message RobotState vide ou avec des valeurs par défaut
        from moveit_msgs.msg import RobotState
        start_state = RobotState()
        return start_state

def main(args=None):
    rclpy.init(args=args)
    trajectory_publisher = TrajectoryPublisher()
    rclpy.spin(trajectory_publisher)
    trajectory_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
