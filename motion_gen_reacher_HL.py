# cuRobo
import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
import torch
from curobo.types.math import Pose
from curobo.types.robot import JointState
from curobo.wrap.reacher.motion_gen import MotionGen, MotionGenConfig, MotionGenPlanConfig
import json


client = mqtt.Client()
client.connect("localhost",1883,60)

world_config = {
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

motion_gen_config = MotionGenConfig.load_from_robot_config(
    "/pkgs/curobo_doosan/src/m1013/m1013.yml",
    world_config,
    interpolation_dt=0.01,
)
motion_gen = MotionGen(motion_gen_config)
motion_gen.warmup()

retract_cfg = motion_gen.get_retract_config()

state = motion_gen.rollout_fn.compute_kinematics(
    JointState.from_position(retract_cfg.view(1, -1))
)

goal_pose = Pose.from_list([-0.4, 0.0, 0.4, 1.0, 0.0, 0.0, 0.0])  # x, y, z, qw, qx, qy, qz
start_state = JointState.from_position(
    torch.zeros(1, 6).cuda(),
    joint_names=['joint1', 'joint2', 'joint3', 'joint4', 'joint5','joint6']
)

result = motion_gen.plan_single(start_state, goal_pose, MotionGenPlanConfig(max_attempts=1))
traj = result.get_interpolated_plan()  # result.optimized_dt has the dt between timesteps

traj_data = {
    "velocity": traj.velocity.tolist()
}

traj_json = json.dumps(traj_data)
# print(f"Trajectory Generated: {traj} ")
client.publish("Velocity", traj_json)
print("Just published " + str(traj_json) + " to Topic Velocity")
time.sleep(10)
client.disconnect()