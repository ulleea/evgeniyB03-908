class Vector():
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self, other):
        return Vector((self.x + other.x), (self.y + other.y),(self.z+other.z))

    def __sub__(self, other):
        return Vector((self.x - other.x), (self.y - other.y),(self.z-other.z))

    def __mul__(self, other):
        return Vector((self.x * other.x), (self.y*other.y),(self.z*other.z))

    def __truediv__(self, a):
        return Vector((self.x/a),(self.y/a),(self.z/a))

    def __abs__(self):
        return (((self.x) ** 2 + (self.y) ** 2+(self.z)**2) ** (1 / 2))

    def cort(self):
        return '('+str(self.x)+','+str(self.y)+','+str(self.z)+')'
    def vect(self,other):
        return Vector((self.y*other.z-self.z*other.y),(-(self.x*other.z-self.z*other.x)),(self.x*other.y-self.y*other.x))


def longest_distance():
    n=int(input())
    max=0
    for i in range(n):
        s=input().split(',')
        a=Vector(int(s[0]),int(s[1]),int(s[2]))
        c=abs(a)
        if c>max:
            max=c
            maxcor=a.cort()
    print(max)
    print(maxcor)
def center_of_mass():
    n = int(input())
    s = input().split(',')
    d = Vector(int(s[0]), int(s[1]), int(s[2]))
    for i in range(n-1):
        s=input().split(',')
        a = Vector(int(s[0]), int(s[1]), int(s[2]))
        d+=a
    d=d/n
    d=d.cort()
    print(d)
def area():
    s1= input().split(',')
    s2= input().split(',')
    a = Vector(int(s1[0]), int(s1[1]), int(s1[2]))
    b = Vector(int(s2[0]), int(s2[1]), int(s2[2]))
    s=abs(a.vect(b))
    print(s)
def volume():
    s1 = input().split(',')
    s2 = input().split(',')
    s3 = input().split(',')
    a = Vector(int(s1[0]), int(s1[1]), int(s1[2]))
    b = Vector(int(s2[0]), int(s2[1]), int(s2[2]))
    c = Vector(int(s3[0]), int(s3[1]), int(s3[2]))
    s = abs(c*(a.vect(b)))
    print(s)

def perimeter():
    n = int(input())
    arr=[]
    for i in range(n):
        s=input().split(',')
        a=Vector(int(s[0]),int(s[1]),int(s[2]))
        arr.append(a)
    max=0
    for i in arr:
        for j in arr:
            l1=abs(i-j)
            for k in arr:
                l2=abs(i-k)
                l3=abs(j-k)
                p=l1+l2+l3
                if p>max:
                    max=p
                    a1=i
                    a2=j
                    a3=k
    s=(a1.cort(),a2.cort(),a3.cort())
    print(max,s)
def max_area():
    n=int(input())
    max=0
    arr=[]
    for i in range(n):
        s = input().split(',')
        a = Vector(int(s[0]), int(s[1]), int(s[2]))
        arr.append(a)
    for k in range(n):
        for i in range(k,n,1):
            a=arr[k]-arr[i]
            for j in range(i,n,1):
                b=arr[k]-arr[j]
                s=abs(a.vect(b))/2
                if s>max:
                    max=s
                    a1=arr[k]
                    a2=arr[i]
                    a3=arr[j]
    s=(a1.cort(),a2.cort(),a3.cort())
    print(max,s)
