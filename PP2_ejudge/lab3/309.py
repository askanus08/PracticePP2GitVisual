import math
class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pow(self.r,2)*3.14159
radius = int(input())
a = Circle(radius)
print(f"{a.area():.2f}")    