

import os

import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument #, SetEnvironmentVariable
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    world_file_name = 'lab.world'
    package_dir = get_package_share_directory('multi_robot')
    gazebo_ros = get_package_share_directory('gazebo_ros')

    gazebo_client = launch.actions.IncludeLaunchDescription(
	launch.launch_description_sources.PythonLaunchDescriptionSource(
            os.path.join(gazebo_ros, 'launch', 'gzclient.launch.py')),
        condition=launch.conditions.IfCondition(launch.substitutions.LaunchConfiguration('gui'))
     )
    gazebo_server = launch.actions.IncludeLaunchDescription(
        launch.launch_description_sources.PythonLaunchDescriptionSource(
            os.path.join(gazebo_ros, 'launch', 'gzserver.launch.py'))
    )
    print(os.path.join(package_dir, 'worlds/', world_file_name))
    return LaunchDescription([
        DeclareLaunchArgument(
          'world',
          default_value=[os.path.join(package_dir, 'worlds/', world_file_name), ''],
          description='SDF world file'),
        DeclareLaunchArgument(
            name='gui',
            default_value='false'
        ),
        DeclareLaunchArgument(
            name='use_sim_time',
            default_value='true'
        ),
        DeclareLaunchArgument('state',
            default_value='true',
            description='Set "true" to load "libgazebo_ros_state.so"'),
        gazebo_server,
        gazebo_client,
    ])


if __name__ == '__main__':
    generate_launch_description()
