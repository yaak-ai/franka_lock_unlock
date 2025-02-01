from setuptools import find_packages, setup

package_name = 'franka_lock_unlock'

setup(
    name=package_name,
    version='5.7.2',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Maxime Borges',
    maintainer_email='maxime@yaak.ai',
    description='Lock or unlock the Franka Research 3 joint brakes programmatically.',
    license='AGPLv3',
    entry_points={
        'console_scripts': [
            'fci = franka_lock_unlock.fci_node:main'
        ],
    },
)
