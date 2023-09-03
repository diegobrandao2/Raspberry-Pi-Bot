import rclpy
import RPi.GPIO as GPIO
from rclpy.node import Node

from geometry_msgs.msg import Twist


class VelocitySubscriber(Node):

    def __init__(self):
        super().__init__('cmd_vel_subscriber')
        self.subscription = self.create_subscription(Twist,'cmd_vel',self.cmd_to_pwm_callback,10)
        self.subscription  # prevent unused variable warning
        
        right_motor_a = 24
        right_motor_b = 23
        right_motor_en = 25

        left_motor_a = 17
        left_motor_b = 18
        left_motor_en = 4

        self.mr_a = right_motor_a
        self.mr_b = right_motor_b
        self.ml_a = left_motor_a
        self.ml_b = left_motor_b

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(right_motor_a, GPIO.OUT)
        GPIO.setup(right_motor_b, GPIO.OUT)
        GPIO.setup(right_motor_en, GPIO.OUT)
        GPIO.setup(left_motor_a, GPIO.OUT)
        GPIO.setup(left_motor_b, GPIO.OUT)
        GPIO.setup(left_motor_en, GPIO.OUT)

        self.pwm_r = GPIO.PWM(right_motor_en, 1000)
        self.pwm_l = GPIO.PWM(left_motor_en, 1000)

        self.pwm_r.start(30)
        self.pwm_l.start(30)

    def cmd_to_pwm_callback(self, msg):
        #self.get_logger().info('I heard: "%s"' % msg.data)
        right_wheel_vel = (msg.linear.x + msg.angular.z) / 2
        left_wheel_vel = (msg.linear.x - msg.angular.z) / 2

        print(right_wheel_vel, " / ",left_wheel_vel)

        GPIO.output(self.mr_a,right_wheel_vel > 0)
        GPIO.output(self.mr_b,right_wheel_vel < 0)
        GPIO.output(self.ml_a,left_wheel_vel > 0)
        GPIO.output(self.ml_b,left_wheel_vel < 0)








def main(args=None):
    rclpy.init(args=args)

    velocity_subscriber = VelocitySubscriber()

    rclpy.spin(velocity_subscriber)

    
    velocity_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()