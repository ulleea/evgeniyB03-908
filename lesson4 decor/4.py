import datetime
def decor(func):
    def upfunc(a,b,path):
        start=datetime.datetime.now()
        n=func(a,b)
        a=[a,b,path]
        end=datetime.datetime.now()
        print(a,start,n,end)
        with open(path,'w') as file:
            l=end-start
            start=str(start)+'\n'
            a=str(a)+'\n'
            n=str(n)+'\n'
            end=str(end)+'\n'
            l=str(l)+'\n'
            file.write(start)
            file.write(a)
            file.write(n)
            file.write(end)
            file.write(l)
    return upfunc
def via(a,b):
    print(a)
    print(b)
    for i in range (10):
        a=a*2
    return a
s=input()
a,b=input().split()
a=int(a)
b=int(b)
f=decor(via)
f(a,b,s)