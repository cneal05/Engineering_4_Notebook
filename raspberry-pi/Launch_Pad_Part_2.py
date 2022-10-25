#type: ignore
import time
import board
import digitalio
#defining the two leds that I will be using 
led1 = digitalio.DigitalInOut(board.GP13)
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP20)
led2.direction = digitalio.Direction.OUTPUT

#counter counts down from 10 to 0 
for counter in range(10, 0, -1):
    print(counter)
    led1.value = True
    time.sleep(1)
    led1.value = False
    time.sleep(1)    
print("Liftoff!")
led2.value = True
time.sleep(3)