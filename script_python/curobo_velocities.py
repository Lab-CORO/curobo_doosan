#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import subprocess

class VelocityNode(Node):
    def __init__(self):
        super().__init__('VelocityNode')
        
    def execute_script_and_capture_output(self):
        try:
            process = subprocess.Popen(['$omni_python', '/pkgs/curobo/examples/isaac_sim/motion_gen_reacher.py'],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       universal_newlines=True)
            stdout, stderr = process.communicate(timeout=500)  
            return_code = process.returncode
            
            if return_code == 0:
                self.get_logger().info(f'Script executed successfully. Output:\n{stdout}')
            else:
                self.get_logger().error(f'Script failed with return code {return_code}. Error:\n{stderr}')
        
        except subprocess.TimeoutExpired:
            self.get_logger().error('Timeout expired while executing the script.')

def main(args=None):
    rclpy.init(args=args)
    node = VelocityNode()
    node.execute_script_and_capture_output()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
