# drone_posn_hold
This repo is intended to provide position data to a onboard flight controller (PX4/CubePilot) from a motion capture system (vicon/optitrack). The intention was to provide a local position hold to enable better data collection for system identification purposes.

Steps to using this package:
Download optitrack/vicon package here (https://github.com/MOCAP4ROS2-Project), download mavros package here (https://github.com/mavlink/mavros).
Add this package and ensure all dependencies are set appropriately. 
Relay local position from motion capture data to ardupilot using set_local_posn.py
Additionally command position to ardupilot using cmd_local_posn.py
All necessary packages are launched from local_posn_launch.py

Follow all Q Ground Control instructions here: 
https://docs.px4.io/main/en/ros/external_position_estimation.html
