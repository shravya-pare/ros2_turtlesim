import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import math

class CircleDrawer(Node):

    def __init__(self):
        super().__init__('circle_drawer')
        self.turtle_publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)

    def draw_circle(self):
        radius = 2.0
        angular_speed = 1.0
        linear_speed = angular_speed * radius
        duration = 10.0  # Time to complete one circle (adjust as needed)

        move_cmd = Twist()
        move_cmd.angular.z = angular_speed  # Start turning

        start_time = time.time()

        while time.time() - start_time < duration:
            self.turtle_publisher.publish(move_cmd)

        # Stop turning
        move_cmd.angular.z = 0.0
        self.turtle_publisher.publish(move_cmd)

    def move_along_circle(self):
        radius = 2.0
        angular_speed = 1.0
        linear_speed = angular_speed * radius

        move_cmd = Twist()
        move_cmd.linear.x = linear_speed  # Start moving forward
        move_cmd.angular.z = angular_speed  # Start turning

        while not self.destroyed:
            self.turtle_publisher.publish(move_cmd)

    def cleanup(self):
        self.destroy_node()
        rclpy.shutdown()

def main():
    rclpy.init()
    circle_drawer = CircleDrawer()

    # Draw a circle
    circle_drawer.draw_circle()

    # Move continuously along the circle
    circle_drawer.move_along_circle()

    # Clean up
    circle_drawer.cleanup()

if __name__ == '__main__':
    main()
