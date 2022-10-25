# type: ignore
import adafruit_mpu6050
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import adafruit_mpl3115a2
import displayio
import busio
import board
import time
import digitalio
displayio.release_displays()
#assigns the scl to GP6 and assigns sda to GP7 on the pico board
sda_pin = board.GP6
scl_pin = board.GP7
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68 )
led = digitalio.DigitalInOut(board.GP20)
led.direction = digitalio.Direction.OUTPUT
sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x60)
display_bus = displayio.I2CDisplay(i2c, device_address= 0x3d, reset=board.GP15)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
initial = sensor.altitude 


while True:
        new = sensor.altitude - initial
        splash = displayio.Group()
        title = "ANGULAR VELOCITY"
        text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=10)
        splash.append(text_area)  
        title = "x = %s" % mpu.acceleration[0] 
        text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=25)
        splash.append(text_area)   
        display.show(splash)
        title = "y = %s" % mpu.acceleration[1] 
        text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=40)
        splash.append(text_area)   
        display.show(splash)
        title = "z = %s" % mpu.acceleration[2]  
        text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=55)
        splash.append(text_area)   
        display.show(splash)
        
        #code below was used to check the difference between the initial and new altitude and would display it to the screen.
        #title = "altitude = %s" % sensor.altitude 
        #text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=40)
        #splash.append(text_area)   
        #display.show(splash)
        #title = "new = %s" % new 
        #text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=55)
        #splash.append(text_area)   
        #display.show(splash)
        #title = "initial = %s" % initial 
        #text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=25)
        #splash.append(text_area)   
        #display.show(splash)

        if new <= 3:
            #checks if the x and y values are above 9.8 or below -9.8
            if mpu.acceleration[0] > 9 or  mpu.acceleration[0] < -9 or mpu.acceleration[1] > 9 or  mpu.acceleration[1] < -9: 
                led.value = True
        time.sleep(1)
        led.value = False