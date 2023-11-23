import rclpy
from geometry_msgs.msg import Twist
import time
import math

def draw_circle(turtle_publisher):
    radius = 1.0
    angular_speed = 2.0  # Increase the angular speed for faster rotation
    linear_speed = angular_speed * radius  # Linear speed for forward movement
    duration = 6.28 / angular_speed  # Circumference / angular speed

    move_cmd = Twist()
    move_cmd.angular.z = angular_speed  # Start turning
    move_cmd.linear.x = linear_speed  # Start moving forward

    start_time = time.time()

    while time.time() - start_time < duration:
        turtle_publisher.publish(move_cmd)

    # Stop turning and moving forward
    move_cmd.angular.z = 0.0
    move_cmd.linear.x = 0.0
    turtle_publisher.publish(move_cmd)

def main():
    rclpy.init()

    node = rclpy.create_node('circle_drawer')
    turtle_publisher = node.create_publisher(Twist, 'turtle1/cmd_vel', 10)

    # Draw a circle
    draw_circle(turtle_publisher)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

