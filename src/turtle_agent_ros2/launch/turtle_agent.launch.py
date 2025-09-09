from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtle_agent',
            executable='turtle_agent',
        ),        
        Node(
            package='turtlesim',
            executable='turtlesim_node',
        )
    ])
