#type: ignore
def calculate(x1,y1,x2,y2,x3,y3):
    area1 = x1*(y2-y3)
    area2 = x2*(y3-y1)
    area3 = x3*(y1-y2)
    areaF = (area1 + area2 + area3)/2
    return areaF

hile True:
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