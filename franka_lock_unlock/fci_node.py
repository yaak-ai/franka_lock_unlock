import rclpy
from rclpy.node import Node
from threading import Event

from franka_lock_unlock.franka_lock_unlock import FrankaLockUnlock

class FrankaLockUnlockNode(Node):
    def __init__(self):
        super().__init__('franka_lock_unlock_node')

        self.declare_parameter('hostname', '192.168.19.2')
        hostname: str = self.get_parameter('hostname').get_parameter_value().string_value
        self.declare_parameter('username', 'franka')
        username: str = self.get_parameter('username').get_parameter_value().string_value
        self.declare_parameter('password', 'franka123')
        password: str = self.get_parameter('password').get_parameter_value().string_value

        franka_lock_unlock = FrankaLockUnlock(hostname=hostname, username=username, password=password, relock=True)
        franka_lock_unlock.run(unlock=True, wait=True, persistent=True, fci=True, execution_mode=True)

        print("Keeping persistent connection...")
        Event().wait()


def main(args=None):
    """
    The main function.
    :param args: Not used directly by the user, but used by ROS2 to configure certain aspects of the Node.
    """
    try:
        rclpy.init(args=args)

        node = FrankaLockUnlockNode()

        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()