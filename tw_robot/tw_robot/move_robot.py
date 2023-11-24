 #!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import transforms3d
import math
from sensor_msgs.msg import LaserScan
    
class GotoGoalNode(Node):
    def __init__(self):
        super().__init__("move_rob")
        self.target_x = 1
        self.target_y = 1
        self.publisher = self.create_publisher(Twist, "cmd_vel", 1)
        # self.subscriber = self.create_subscription(Odometry, "odom", self.control_loop, 10)
        self.subscriber1=self.create_subscription(LaserScan,"gazebo_lidar/out",self.value_loop,1)
               
    def value_loop(self, msg):
        vel=Twist()
        
        for i in range(158,221):
            print(msg.ranges[i])
        
        if (str(msg.ranges[158]) == 'inf'):
            vel.linear.x = 0.5
            vel.angular.z = 0.0
            
        self.publisher.publish(vel)
        
def main(args=None):
    rclpy.init(args=args)
    node = GotoGoalNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == "__main__":
	main()
