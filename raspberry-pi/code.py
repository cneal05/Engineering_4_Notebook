# type: ignore
import adafruit_mpu6050
import busio
import board
import time
import digitalio

sda_pin = board.GP6
scl_pin = board.GP7
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)
led = digitalio.DigitalInOut(board.GP20)
led.direction = digitalio.Direction.OUTPUT

while True:
    print(mpu.acceleration)
    if mpu.acceleration[0] > 9 or  mpu.acceleration[0] < -9 or mpu.acceleration[1] > 9 or  mpu.acceleration[1] < -9: 
            print("SPIN")
            led.value = True
            led.value = False
    time.sleep(1)