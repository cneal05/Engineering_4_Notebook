#type: ignore
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio
import board
import busio
displayio.release_displays()

sda_pin = board.GP6
scl_pin = board.GP7
i2c = busio.I2C(scl_pin, sda_pin)
display_bus = displayio.I2CDisplay(i2c, device_address= 0x3d, reset=board.GP15)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

def calculate(x1,y1,x2,y2,x3,y3):
    area1 = x1*(y2-y3)
    area2 = x2*(y3-y1)
    area3 = x3*(y1-y2)
    areaF = (area1 + area2 + area3)/2
    return areaF

while True:
    print("Enter the first coordinate in format x,y:")
    answer1 = input()
    a1List = answer1.split(",")
    print("Enter the second coordinate in format x,y:")
    answer2 = input()
    a2List = answer2.split(",")
    print("Enter the third coordinate in format x,y:")
    answer3 = input()
    a3List = answer3.split(",")
    try:
        x1 = float(a1List[0])
        x2 = float(a2List[0])
        x3 = float(a3List[0])
        y1 = float(a1List[1])
        y2 = float(a2List[1])
        y3 = float(a3List[1])
        area = calculate(x1,y1,x2,y2,x3,y3)
        areafinal = abs(area)
        print(f"The area of the triangle with vertices ({x1},{y1}), ({x2},{y2}), ({x3},{y3}) is {areafinal} square km")
    except:
        print("wrong format, please enter coordinates in the correct formatting")
       
    splash = displayio.Group()
    linex1 = 64
    liney1 = 0
    linex2 = 64
    liney2 = 64
    hline = Line(linex1,liney1,linex2,liney2, color=0xFFFF00)
    splash.append(hline)
    display.show(splash)
   
    linex1 = 0
    liney1 = 32
    linex2 = 128
    liney2 = 32
    hline = Line(linex1,liney1,linex2,liney2, color=0xFFFF00)
    splash.append(hline)
    display.show(splash)

    x1 = int(a1List[0]) + 64
    x2 = int(a2List[0]) + 64
    x3 = int(a3List[0]) + 64
    #print(a1List[1])
    #print(a2List[1])
    #print(a3List[1])
    y1 = -1*int(a1List[1]) + 32
    y2 = -1*int(a2List[1]) + 32
    y3 = -1*int(a3List[1]) + 32
    triangle = Triangle(x1, y1, x2, y2, x3, y3, outline=0xFFFF00)
    splash.append(triangle)
    display.show(splash)
