#type: ignore
import time
import board
import digitalio
led1 = digitalio.DigitalInOut(board.GP13)
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP20)
led2.direction = digitalio.Direction.OUTPUT
buttonPin = digitalio.DigitalInOut(board.GP28)
buttonPin.direction = digitalio.Direction.INPUT
buttonPin.pull = digitalio.Pull.DOWN 

while True:
    if buttonPin.value == True:
        print(buttonPin.value)
        for counter in range(10, 0, -1):
            print(counter)
            led1.value = True
            time.sleep(0.5)
            led1.value = False
            time.sleep(0.5)    
        print("Liftoff!")
        led2.value = True
        time.sleep(3)