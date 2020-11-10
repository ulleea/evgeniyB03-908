def decor(func):
    def func_1(*a):
        m=a[::-1]
        func(*m)
    return func_1
def pr(*a):
    print(*a)

s=input().split()
pr=decor(pr)
pr(*s)