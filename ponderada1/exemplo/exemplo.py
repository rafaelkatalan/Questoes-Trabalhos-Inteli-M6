#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import math


class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 100)
        self.timer_ = self.create_timer(0.1, self.move_turtle)
        self.twist_msg_ = Twist()

    def move_turtle(self):
        for i in range(5):
            # Move a distância de um lado do quadrado
            self.twist_msg_.linear.x = 2.0
            self.twist_msg_.angular.z = 0.0
            self.publisher_.publish(self.twist_msg_)
            time.sleep(2)

            # Vira 90 graus
            self.twist_msg_.linear.x = 0.0
            self.twist_msg_.angular.z = math.pi/2.5
            self.publisher_.publish(self.twist_msg_)
            time.sleep(2)
        
        self.twist_msg_.linear.x = 0.5
        self.twist_msg_.angular.z = 0.0
        self.publisher_.publish(self.twist_msg_)
        time.sleep(2)
        self.twist_msg_.linear.x = 0.0
        self.twist_msg_.angular.z = -0.1+math.pi/2
        self.publisher_.publish(self.twist_msg_)
        time.sleep(2)
        self.twist_msg_.linear.x = -2.0
        self.twist_msg_.angular.z = 0.0
        self.publisher_.publish(self.twist_msg_)
        time.sleep(2)
        self.twist_msg_.linear.x = 0.0
        self.twist_msg_.angular.z = math.pi/2
        self.publisher_.publish(self.twist_msg_)
        time.sleep(2)
        self.twist_msg_.linear.x = -1.0
        self.twist_msg_.angular.z = 0.0
        self.publisher_.publish(self.twist_msg_)
        time.sleep(2)
        self.twist_msg_.linear.x = 0.0
        self.twist_msg_.angular.z = math.pi/2
        self.publisher_.publish(self.twist_msg_)
        time.sleep(2)
        self.twist_msg_.linear.x = -2.0
        self.twist_msg_.angular.z = 0.0
        self.publisher_.publish(self.twist_msg_)
        time.sleep(2)
        self.twist_msg_.linear.x = 0.0
        self.twist_msg_.angular.z = -0.01+math.pi/2
        self.publisher_.publish(self.twist_msg_)
        time.sleep(2)
        self.twist_msg_.linear.x = -1.5
        self.twist_msg_.angular.z = 0.0
        self.publisher_.publish(self.twist_msg_)
        time.sleep(2)

def main(args=None):
    rclpy.init()
    turtle_controller = TurtleController()
    rclpy.spin(turtle_controller)
    turtle_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
