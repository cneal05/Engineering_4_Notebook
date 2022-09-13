#type: ignore
import adafruit_mpu6050
import busio
import board

sda_pin = board.GP6
scl_pin = board.GP7
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)
print(mpu.acceleration)