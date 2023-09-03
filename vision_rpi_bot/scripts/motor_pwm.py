import RPi.GPIO as GPIO
import time


right_motor_a = 24
right_motor_b = 23
right_motor_en = 25

left_motor_a = 17
left_motor_b = 18
left_motor_en = 4

GPIO.setmode(GPIO.BCM)

GPIO.setup(right_motor_a, GPIO.OUT)
GPIO.setup(right_motor_b, GPIO.OUT)
GPIO.setup(right_motor_en, GPIO.OUT)

GPIO.setup(left_motor_a, GPIO.OUT)
GPIO.setup(left_motor_b, GPIO.OUT)
GPIO.setup(left_motor_en, GPIO.OUT)

pwm_r = GPIO.PWM(right_motor_en, 1000)
pwm_l = GPIO.PWM(left_motor_en, 1000)

pwm_r.start(30)
pwm_l.start(30)


def forward(second):
    print("moving forward")
    GPIO.output(right_motor_a,GPIO.HIGH)
    GPIO.output(right_motor_b,GPIO.LOW)
    GPIO.output(left_motor_a,GPIO.HIGH)
    GPIO.output(left_motor_b,GPIO.LOW)
    time.sleep(second)


def reverse(second):
    print("moving reverse")
    GPIO.output(right_motor_a,GPIO.LOW)
    GPIO.output(right_motor_b,GPIO.HIGH)
    GPIO.output(left_motor_a,GPIO.LOW)
    GPIO.output(left_motor_b,GPIO.HIGH)
    time.sleep(second)

def left(second):
    print("turning left")
    GPIO.output(right_motor_a,GPIO.HIGH)
    GPIO.output(right_motor_b,GPIO.LOW)
    GPIO.output(left_motor_a,GPIO.LOW)
    GPIO.output(left_motor_b,GPIO.HIGH)
    time.sleep(second)

def right(second):
    print("turning right")
    GPIO.output(right_motor_a,GPIO.LOW)
    GPIO.output(right_motor_b,GPIO.HIGH)
    GPIO.output(left_motor_a,GPIO.HIGH)
    GPIO.output(left_motor_b,GPIO.LOW)
    time.sleep(second)

def stop():
    print("stopping")
    pwm_l.ChangeDutyCycle(0)
    pwm_r.ChangeDutyCycle(0)
  

def exit():
    GPIO.cleanup()

def main():
    forward(2)
    reverse(2)
    left(3)
    right(3)
    stop()
    exit()

if __name__ == '__main__':
    main()