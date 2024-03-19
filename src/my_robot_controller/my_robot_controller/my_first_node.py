import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class MyNode(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer_ = self.create_timer(1.0, self.send_commands)
        
        # Linear velocity for moving forward (m/s)
        self.linear_speed = 6.0
        
        # Angular velocity for turning (rad/s)
        self.angular_speed = 2.0

    def send_commands(self):
        twist = Twist()
        
        # Set linear velocity for moving forward
        twist.linear.x = self.linear_speed
        
        # Set angular velocity for turning (positive for clockwise, negative for counterclockwise)
        twist.angular.z = self.angular_speed
        
        self.publisher_.publish(twist)


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
