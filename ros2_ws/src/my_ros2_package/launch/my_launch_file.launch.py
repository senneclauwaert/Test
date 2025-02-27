#!/usr/bin/env python3
import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='my_ros2_package',
            executable='segmentation_node',  # The name of your executable (see below)
            name='segmentation_node'
        ),
        launch_ros.actions.Node(
            package='my_ros2_package',
            executable='navigation_node',  # The name of your executable (see below)
            name='navigation_node'
        )
    ])
