import math
class Shape(object):
    def area(self):
        pass

class Rect(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height= height

    def area(self):
        return self.height * self.width

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi*self.radius**2

myshapes=[Rect(1.0,2.0),Rect(2.0,4.0),Circle(5.0)]
sum_shapes=0.0
for shape in myshapes:
    sum_shapes+=shape.area()
print myshapes[0].area()
print myshapes[1].area()
print myshapes[2].area()
print sum_shapes
