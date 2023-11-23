import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import math
import threading
import signal

class TriangleDrawer(Node):

    def __init__(self):
        super().__init__('triangle_drawer')
        self.turtle_publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.is_running = True  # Flag to control whether the drawing should continue
        self.draw_thread = threading.Thread(target=self.draw_equilateral_triangle)

    def draw_equilateral_triangle(self):
        side_length = 2.0
        angular_speed = 1.0
        turn_angle = 120.0  # turning angle of an equilateral triangle

        move_cmd = Twist()

        while self.is_running:
            for _ in range(3):
                # Move forward to draw a side
                move_cmd.linear.x = side_length
                self.turtle_publisher.publish(move_cmd)
                time.sleep(side_length / angular_speed)

                # Stop moving forward
                move_cmd.linear.x = 0.0
                self.turtle_publisher.publish(move_cmd)
                time.sleep(1)

                # Turn to the next side (equilateral triangle has interior angles of 60 degrees)
                move_cmd.angular.z = math.radians(turn_angle)
                self.turtle_publisher.publish(move_cmd)
                time.sleep(1)

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
    triangle_drawer = TriangleDrawer()

    # Set up signal handler to capture termination signals
    signal.signal(signal.SIGINT, signal_handler)

    try:
        # Start drawing in a separate thread
        triangle_drawer.start_drawing()

        # Keep the program running until termination signal is received
        rclpy.spin(triangle_drawer)
    finally:
        # Stop drawing
        triangle_drawer.stop_drawing()
        # Clean up
        triangle_drawer.cleanup()

if __name__ == '__main__':
    main()
