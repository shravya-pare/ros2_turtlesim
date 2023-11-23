import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import math
import threading
import signal

class SquareDrawer(Node):

    def __init__(self):
        super().__init__('square_drawer')
        self.turtle_publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.is_running = True  # Flag to control whether the drawing should continue
        self.draw_thread = threading.Thread(target=self.draw_square)

    def draw_square(self):
        side_length = 2.0
        angular_speed = 9.0
        linear_speed = 10.0  # Increase linear speed for faster linear movement
        turn_angle = 90.0  # turning angle of a square

        move_cmd = Twist()

        while self.is_running:
            for _ in range(4):
                # Move forward to draw a side
                move_cmd.linear.x = linear_speed * side_length
                move_cmd.linear.y = 0.0
                move_cmd.linear.z = 0.0
                move_cmd.angular.x = 0.0
                move_cmd.angular.y = 0.0
                move_cmd.angular.z = 0.0
                self.turtle_publisher.publish(move_cmd)
                time.sleep(side_length / linear_speed)

                # Stop moving forward
                move_cmd.linear.x = 0.0
                self.turtle_publisher.publish(move_cmd)
                time.sleep(1)

                # Turn to the next side (square has interior angles of 90 degrees)
                move_cmd.angular.z = math.radians(turn_angle)
                self.turtle_publisher.publish(move_cmd)
                time.sleep(1 / angular_speed)

                # Stop turning
                move_cmd.angular.z = 0.0
                self.turtle_publisher.publish(move_cmd)
                time.sleep(1)

    def start_drawing(self):
        self.draw_thread.start()

    def stop_drawing(self):
        self.is_running = False
        self.draw_thread.join()  # Wait for the drawing thread to finish

    def cleanup(self):
        self.destroy_node()
        rclpy.shutdown()

def signal_handler(sig, frame):
    # Handle termination signals (e.g., Ctrl+C)
    rclpy.shutdown()

def main():
    rclpy.init()

    square_drawer = SquareDrawer()

    # Set up signal handler to capture termination signals
    signal.signal(signal.SIGINT, signal_handler)

    try:
        # Start drawing in a separate thread
        square_drawer.start_drawing()

        # Keep the program running until termination signal is received
        rclpy.spin(square_drawer)
    finally:
        # Stop drawing
        square_drawer.stop_drawing()
        # Clean up
        square_drawer.cleanup()

if __name__ == '__main__':
    main()

