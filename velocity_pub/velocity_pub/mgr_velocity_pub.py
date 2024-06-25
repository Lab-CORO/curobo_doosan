#!/isaac-sim/kit/python/bin/python3

import rclpy
from rclpy.node import Node
from curobo.types.math import Pose
from curobo.types.robot import JointState
from curobo.wrap.reacher.motion_gen import MotionGen, MotionGenConfig, MotionGenPlanConfig
import torch

class MyNode(Node):
    def __init__(self):
        super().__init__('mgr_velocity_node')
        
        # Initialize motion planning components
        world_config = {
            "mesh": {
                "base_scene": {
                    "pose": [10.5, 0.080, 1.6, 0.043, -0.471, 0.284, 0.834],
                    "file_path": "scene/nvblox/srl_ur10_bins.obj",
                },
            },
            "cuboid": {
                "table": {
                    "dims": [5.0, 5.0, 0.2],
                    "pose": [0.0, 0.0, -0.1, 1, 0, 0, 0.0],
                },
            },
        }
        
        motion_gen_config = MotionGenConfig.load_from_robot_config(
            "/pkgs/curobo_doosan/src/m1013/m1013.yml",
            world_config,
            interpolation_dt=0.01,
        )
        self.motion_gen = MotionGen(motion_gen_config)
        self.motion_gen.warmup()
        
        # Example using Torch
        start_state = JointState.from_position(
            torch.zeros(1, 6).cuda(),
            joint_names=['joint1', 'joint2', 'joint3', 'joint4', 'joint5','joint6'],
        )
        
        goal_pose = Pose.from_list([-0.4, 0.0, 0.4, 1.0, 0.0, 0.0, 0.0])
        
        result = self.motion_gen.plan_single(start_state, goal_pose, MotionGenPlanConfig(max_attempts=1))
        traj = result.get_interpolated_plan()
        
        self.get_logger().info(f"Trajectory Generated: {result.success} is {traj}")
        
def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
