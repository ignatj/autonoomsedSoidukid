from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    goal_pose_publisher = Node(
        package='my_robot_controller',
        executable='navigation',
        name='navigation')

    ld = LaunchDescription()

    ld.add_action(goal_pose_publisher)

    return ld