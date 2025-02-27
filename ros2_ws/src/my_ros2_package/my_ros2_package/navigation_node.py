#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class NavigationNode(Node):
    def __init__(self):
        super().__init__('navigation_node')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        # Timer to publish commands every second
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info("Navigation node has started.")

    def timer_callback(self):
        # Dummy navigation: always move forward slowly.
        twist = Twist()
        twist.linear.x = 0.1  # forward speed (m/s)
        twist.angular.z = 0.0  # no rotation
        self.publisher.publish(twist)
        self.get_logger().info("Published navigation command.")

def main(args=None):
    rclpy.init(args=args)
    node = NavigationNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
