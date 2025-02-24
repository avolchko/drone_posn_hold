import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped

# read in optitrack, send to mavros

class MinimalSubPub(Node):

    def __init__(self):
        super().__init__('minimal_subpub')
        self.publisher_ = self.create_publisher(PoseStamped, '/mavros/vision_pose/pose', 10)
        self.subscription = self.create_subscription(PoseStamped, '/msg_rb', self.listener_callback, 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = PoseStamped()

        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "map"

        msg.pose.position.x = 1.0
        msg.pose.position.y = 2.0
        msg.pose.position.z = 3.0

        msg.pose.orientation.x = 0.0
        msg.pose.orientation.y = 0.0
        msg.pose.orientation.z = 0.0
        msg.pose.orientation.w = 1.0

        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%f"' % msg.pose.position.x)
        self.i += 1


    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%f"' % msg.pose.position.x)


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