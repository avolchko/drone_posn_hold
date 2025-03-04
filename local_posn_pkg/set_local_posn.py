import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from mocap4r2_msgs.msg import RigidBodies


position_x = 0.0
position_y = 0.0
position_z = 0.0


class MinimalSubPub(Node):


    def __init__(self):
        super().__init__('minimal_subpub')
        # self.publisher_ = self.create_publisher(PoseStamped, '/setpoint_position/local', 10)

        self.publisher_ = self.create_publisher(PoseStamped, '/vision_pose/pose', 10)

        self.subscription = self.create_subscription(RigidBodies, '/rigid_bodies', self.listener_callback, 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        global position_x
        global position_y
        global position_z

        msg = PoseStamped()

        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "map"


        # remap appropriately
        msg.pose.position.x = position_x
        msg.pose.position.y = position_z
        msg.pose.position.z = - position_y


        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%f"' % msg.pose.position.x)
        self.i += 1

        # publish to mavros
        # read error from mavros (subscribe to both current local pose and set pose)


    def listener_callback(self, msg):
        self.get_logger().info('I heardmsg.rigidbodies[0].pose.position.x: "%f"' % msg.rigidbodies[0].pose.position.x)
        global position_x 
        global position_y 
        global position_z 

        position_x = msg.rigidbodies[0].pose.position.x
        position_y = msg.rigidbodies[0].pose.position.y
        position_z = msg.rigidbodies[0].pose.position.z

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