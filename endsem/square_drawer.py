import rclpy
from geometry_msgs.msg import Twist
import time
import math

def draw_square(turtle_publisher):
    for _ in range(4):
        move_cmd = Twist()
        move_cmd.linear.x = 2.0  # Increase the forward speed to 2.0
        turtle_publisher.publish(move_cmd)
        time.sleep(1)  # Adjust the duration based on the turtlesim's responsiveness

        move_cmd.linear.x = 0.0  # Stop moving
        turtle_publisher.publish(move_cmd)
        time.sleep(0.5)

        move_cmd.angular.z = math.pi / 2  # Turn with speed pi/2 (90 degrees)
        turtle_publisher.publish(move_cmd)
        time.sleep(1)  # Adjust the duration based on the turtlesim's responsiveness

        move_cmd.angular.z = 0.0  # Stop turning
        turtle_publisher.publish(move_cmd)
        time.sleep(0.5)

def main():
    rclpy.init()

    node = rclpy.create_node('square_drawer')
    turtle_publisher = node.create_publisher(Twist, 'turtle1/cmd_vel', 10)

    draw_square(turtle_publisher)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
