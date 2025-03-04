from launch_ros.substitutions import FindPackageShare

from launch import LaunchDescription 
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution, TextSubstitution

# this file launches optitrack launch file, mavros launch file, and local_posn node
# intended for sending mocap signals as local positioning for quadrotor 
def generate_launch_description():
    return LaunchDescription([
        # include ros node to command position to ardupilot
        Node(
            package='local_posn_pkg',
            namespace='cmd_local_posn',
            executable='cmd_local_posn',
            name='cmd'
        ),

        # include ros node to set local position of ardupilot
        Node(
            package='local_posn_pkg',
            namespace='set_local_posn',
            executable='set_local_posn',
            name='set'
        ),

        # include ros launch file to talk to optitrack
        IncludeLaunchDescription(
                PathJoinSubstitution([
                    FindPackageShare('mocap4r2_optitrack_driver'),
                    'launch',
                    'optitrack2.launch.py'
                ]),
        ),

        # include ros launch file to talk to mavlink
        IncludeLaunchDescription(
                PathJoinSubstitution([
                    FindPackageShare('mavros'),
                    'launch',
                    'apm.launch'
                ]),
        ),



    ])
