'''
15. Define a class named Shape and its subclass Square.
The Square class has an init function which takes a length as argument.
 Both classes have a area function which can print the area of the shape
 where Shape's area is 0 by default.
'''

class Shape:
    def area(self):
        print("Area Of Shape is: ",0)


class Square(Shape):
    def __init__(self,l):
        self.length=l
        print("Length is: ",self.length)

    def area(self):
        print("Area of Square is: ",self.length*self.length)

sh=Shape()
sq=Square(5)
sq.area()