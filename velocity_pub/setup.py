from setuptools import find_packages, setup

package_name = 'velocity_pub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='coro',
    maintainer_email='lucas.carpentier.1@ens.etsmtl.ca',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "joint_velocity_publisher = velocity_pub.velocity_pub:main"
        ],
    },
)
