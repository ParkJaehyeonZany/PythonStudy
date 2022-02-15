import math

class Circle:

    def __init__(self, radius, cx, cy):
        self.radius = radius
        self.cx = cx
        self.cy = cy
    def area(self):
        return (self.radius ** 2) * math.pi
    def center(self):
        return self.cx, self.cy

def main():
    radius = int(input('반지름 : '))
    cx = int(input('x좌표 : '))
    cy = int(input('y좌표 : '))
    circle = Circle(radius, cx, cy)
    print(f"원의 넓이 : {Circle.area(circle)}")
    print(f"중심 좌표 : {Circle.center(circle)}")

main()
