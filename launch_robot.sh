#!/bin/bash

trap "kill 0" SIGINT SIGTERM\n\

roslaunch dsr_ros_control doosan_interface_moveit.launch &

sleep 20

roslaunch unity_ros_doosan moveit_servo_doosan.launch &

sleep 10

rosservice call /controller_manager/load_controller "name: 'dsr_joint_velocity_controller'"

sleep 5

rosservice call /controller_manager/switch_controller "{start_controllers: ['dsr_joint_velocity_controller'], stop_controllers: [], strictness: 1}"
