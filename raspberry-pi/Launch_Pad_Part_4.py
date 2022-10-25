#type: ignore
import time
import board
import digitalio
import pwmio
from adafruit_motor import servo
#defining the two leds that I will be using 
led1 = digitalio.DigitalInOut(board.GP13)
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP20)
led2.direction = digitalio.Direction.OUTPUT
#assigns the button pin to GP28 on the pico board
buttonPin = digitalio.DigitalInOut(board.GP28)
buttonPin.direction = digitalio.Direction.INPUT
buttonPin.pull = digitalio.Pull.DOWN 
#assigning the servo pins to the servo allowing it work
pwm_servo = pwmio.PWMOut(board.GP2, duty_cycle=2 ** 15, frequency=50)
servoPin = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)

while True:
    if buttonPin.value == True:
        servoPin.angle = 0
        print(buttonPin.value)
        #counter counts down from 10 to 0 
        for counter in range(10, 0, -1):
            print(counter)
            led1.value = True
            time.sleep(0.5)
            led1.value = False
            time.sleep(0.5)    
        print("Liftoff!")
        led2.value = True
        servoPin.angle = 180
        time.sleep(3)