import RPi.GPIO as GPIO
import time

# 设置GPIO模式为BCM
GPIO.setmode(GPIO.BCM)

# 假设电机控制引脚为17和18
motor_left_pin = 17
motor_right_pin = 18

# 初始化引脚输出模式
GPIO.setup(motor_left_pin, GPIO.OUT)
GPIO.setup(motor_right_pin, GPIO.OUT)

def forward():
    GPIO.output(motor_left_pin, GPIO.HIGH)
    GPIO.output(motor_right_pin, GPIO.HIGH)
    print("Moving Forward")

def stop():
    GPIO.output(motor_left_pin, GPIO.LOW)
    GPIO.output(motor_right_pin, GPIO.LOW)
    print("Stopping")

# 添加更多函数如backward(), left(), right()...

try:
    forward()
    time.sleep(2) # 前进2秒
    stop()
finally:
    GPIO.cleanup() # 清理GPIO，防止警告或意外行为