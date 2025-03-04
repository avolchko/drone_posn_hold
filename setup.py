from setuptools import find_packages, setup

# import for launch files
import os
from glob import glob

package_name = 'local_posn_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
         (os.path.join('share', package_name, 'launch'), 
         glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools', 'geometry_msgs', 'mavros_msgs', 'mocap_interfaces'],
    zip_safe=True,
    maintainer='bprl',
    maintainer_email='anvo9547@colorado.edu',
    description='Use this package to pull in mocap data, remap appropriately, and send to ardupilot via mavros as local position.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cmd_local_posn = local_posn_pkg.cmd_local_posn:main',
            'set_local_posn = local_posn_pkg.set_local_posn:main',
        ],
    },
)
