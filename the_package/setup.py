from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'the_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shravya',
    maintainer_email='shravya@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'learn = the_package.learn:main',
            'robot_publisher = the_package.robot_publisher:main',
            'robot_sub = the_package.robot_subscriber:main',
            
        ],
    },
)
