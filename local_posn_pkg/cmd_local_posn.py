import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from mocap4r2_msgs.msg import RigidBodies


class MinimalSubPub(Node):

    def __init__(self):
        super().__init__('minimal_subpub')
        self.publisher_ = self.create_publisher(PoseStamped, '/setpoint_position/local', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = PoseStamped()

        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "map"


        # set the position of the drone [m]
        msg.pose.position.x = 1.1
        msg.pose.position.y = 1.2
        msg.pose.position.z = 1.3

        msg.pose.orientation.x = 0.0
        msg.pose.orientation.y = 0.0
        msg.pose.orientation.z = 0.0
        msg.pose.orientation.w = 1.0

        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%f"' % msg.pose.position.x)
        self.i += 1

        # publish to mavros
        # read error from mavros (subscribe to both current local pose and set pose)


def main(args=None):
    rclpy.init(args=args)
    
    minimal_subpub = MinimalSubPub()

    rclpy.spin(minimal_subpub)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subpub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()