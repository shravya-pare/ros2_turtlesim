import rclpy
from geometry_msgs.msg import Twist
import time
import math

def draw_spiral(turtle_publisher):
    angular_speed = 2.0
    linear_speed_start = 0.2
    linear_speed_increment = 0.02
    duration = 20.0

    move_cmd = Twist()
    move_cmd.angular.z = angular_speed  # Start turning

    start_time = time.time()

    while time.time() - start_time < duration:
        move_cmd.linear.x += linear_speed_increment
        turtle_publisher.publish(move_cmd)
        time.sleep(0.1)  # Adjust the sleep duration as needed

    # Stop turning and moving forward
    move_cmd.angular.z = 0.0
    move_cmd.linear.x = 0.0
    turtle_publisher.publish(move_cmd)

def main():
    rclpy.init()

    node = rclpy.create_node('spiral_drawer')
    turtle_publisher = node.create_publisher(Twist, 'turtle1/cmd_vel', 10)

    # Draw a spiral
    draw_spiral(turtle_publisher)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
