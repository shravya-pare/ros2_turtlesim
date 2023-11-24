
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='the_package',
            executable='learn',
            output='screen'),
    ])