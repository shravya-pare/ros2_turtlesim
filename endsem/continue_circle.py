import turtle
import rclpy
from geometry_msgs.msg import Twist
from math import radians

class CircleDrawer:
    def __init__(self, radius):
        self.radius = radius
        self.turtle = turtle.Turtle()
        self.init_ros()

    def init_ros(self):
        rclpy.init()
        self.node = rclpy.create_node('circle_drawer_node')
        self.publisher = self.node.create_publisher(Twist, 'turtle1/cmd_vel', 10)

    def draw_circle(self):
        self.turtle.penup()
        self.turtle.goto(0, -self.radius)
        self.turtle.pendown()
        self.turtle.circle(self.radius)

    def move_along_circumference(self):
        rate = self.node.create_rate(1, 1)  # 1 Hz
        while rclpy.ok():
            msg = Twist()
            msg.linear.x = 0.1  # Adjust the linear velocity as needed
            msg.angular.z = radians(45)  # Adjust the angular velocity as needed
            self.publisher.publish(msg)
            self.node.spin_once()
            rate.sleep()

    def run(self):
        self.draw_circle()
        self.move_along_circumference()

if __name__ == '__main__':
    circle_drawer = CircleDrawer(radius=100)  # Adjust the radius as needed
    try:
        circle_drawer.run()
    except rclpy.exceptions.ROSInterruptException:
        pass
    finally:
        circle_drawer.node.destroy_node()
        rclpy.shutdown()
