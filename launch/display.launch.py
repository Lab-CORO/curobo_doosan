#!/usr/bin/env python3

import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    # Get package directory
    pkg_dir = get_package_share_directory('curobo_doosan')

    # Path to URDF file
    urdf_file = os.path.join(pkg_dir, 'src', 'm1013', 'm1013.urdf')

    # Declare launch arguments
    use_gui = DeclareLaunchArgument(
        'gui',
        default_value='true',
        description='Start joint_state_publisher_gui if true, else joint_state_publisher'
    )

    use_rviz = DeclareLaunchArgument(
        'rviz',
        default_value='true',
        description='Start RViz if true'
    )

    # Read URDF file
    with open(urdf_file, 'r') as f:
        robot_description = f.read()

    # Robot State Publisher node
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': robot_description,
            'use_sim_time': False
        }]
    )

    # Joint State Publisher node (without GUI)
    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        condition=lambda context: 'false' if LaunchConfiguration('gui').perform(context) == 'true' else 'true'
    )

    # Joint State Publisher GUI node
    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        condition=lambda context: 'true' if LaunchConfiguration('gui').perform(context) == 'true' else 'false'
    )

    # RViz node
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', os.path.join(pkg_dir, 'launch', 'robot.rviz')],
        condition=lambda context: 'true' if LaunchConfiguration('rviz').perform(context) == 'true' else 'false'
    )

    return LaunchDescription([
        use_gui,
        use_rviz,
        robot_state_publisher_node,
        joint_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz_node
    ])
