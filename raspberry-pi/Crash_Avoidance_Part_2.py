# type: ignore
import adafruit_mpu6050
import busio
import board
import time
import digitalio
#assigns the scl to GP6 and assigns sda to GP7 on the pico board
sda_pin = board.GP6
scl_pin = board.GP7
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)
led = digitalio.DigitalInOut(board.GP20)
led.direction = digitalio.Direction.OUTPUT

while True:
    print(mpu.acceleration)
    #checks if the x and y values are above 9.8 or below -9.8
    if mpu.acceleration[0] > 9 or  mpu.acceleration[0] < -9 or mpu.acceleration[1] > 9 or  mpu.acceleration[1] < -9: 
            print("SPIN")
            led.value = True
            time.sleep(1)
            led.value = False
    time.sleep(1)