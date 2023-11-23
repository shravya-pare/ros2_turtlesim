import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import math

class TriangleDrawer(Node):

    def __init__(self):
        super().__init__('triangle_drawer')
        self.turtle_publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)

    def draw_equilateral_triangle(self):
        side_length = 2.0
        angular_speed = 1.0
        turn_angle = 120.0  # turning angle of an equilateral triangle

        move_cmd = Twist()

        for _ in range(3):
            # Move forward to draw a side
            move_cmd.linear.x = side_length
            self.turtle_publisher.publish(move_cmd)
            time.sleep(side_length / angular_speed)  # Adjust the sleep duration based on the turtlesim's responsiveness

            # Stop moving forward
            move_cmd.linear.x = 0.0
            self.turtle_publisher.publish(move_cmd)
            time.sleep(1)

            # Turn to the next side (equilateral triangle has interior angles of 60 degrees)
            move_cmd.angular.z = math.radians(turn_angle)
            self.turtle_publisher.publish(move_cmd)
            time.sleep(1)  # Adjust the sleep duration based on the turtlesim's responsiveness

            # Stop turning
            move_cmd.angular.z = 0.0
            self.turtle_publisher.publish(move_cmd)
            time.sleep(1)

    def cleanup(self):
        self.destroy_node()
        rclpy.shutdown()

def main():
    rclpy.init()
    triangle_drawer = TriangleDrawer()

    # Draw an equilateral triangle
    triangle_drawer.draw_equilateral_triangle()

    # Clean up
    triangle_drawer.cleanup()

if __name__ == '__main__':
    main()

