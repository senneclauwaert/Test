#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class SegmentationNode(Node):
    def __init__(self):
        super().__init__('segmentation_node')
        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            10
        )
        self.bridge = CvBridge()
        self.get_logger().info("Segmentation node has started.")

    def image_callback(self, msg):
        try:
            # Convert ROS image message to OpenCV image
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        except Exception as e:
            self.get_logger().error(f"Failed to convert image: {e}")
            return

        # --- Dummy segmentation logic ---
        # Convert image to grayscale and threshold it for demonstration.
        gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        _, segmented = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        # In your implementation, run your trained model here.
        self.get_logger().info("Image segmented.")
        # Optionally, publish or visualize the segmented image.

def main(args=None):
    rclpy.init(args=args)
    node = SegmentationNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
