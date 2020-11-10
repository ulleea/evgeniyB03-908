class Complex():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self, other):
        return Complex((self.a+other.a),(self.b+other.b))
    def __sub__(self, other):
        return Complex((self.a-other.a),(self.b-other.b))
    def __mul__(self, other):
        return Complex((self.a*other.a-self.b*other.b),(self.b*other.a+self.a*other.b))
    def __truediv__(self, other):
        return Complex((self.a*other.a+self.b*other.b)/(other.a**2+other.b**2),(self.b*other.a-self.a*other.b)/(other.a**2+other.b**2))
    def __abs__(self):
        return ((self.a)**2+(self.b)**2)**(1/2)
    def print(self):
        print(str(self.a)+'+'+str(self.b)+'i')
a=Complex(3,4)
a.print()
b=abs(a)
print(b)