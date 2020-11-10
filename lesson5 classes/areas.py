class Shape:
    def __init__(self,h,l):
        self.h=h
        self.l=l


class Triangle (Shape):

    def area(self):
        self.s=self.h*self.l/2
        return self.s


class Rectangle(Shape):

    def area(self):
        self.s=self.h*self.l
        return self.s
a=Shape(2,3)
b=Rectangle(2,3)
print()
print(b.area())
print()
