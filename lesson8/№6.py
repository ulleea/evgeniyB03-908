def func(s,m):
    from itertools import groupby
    a=[]
    for k, g in groupby(s,max):
        a.append(k)
    s=0
    for i in a:
        s+=i**2
    s=s%m
    return s
s=[[1,2,3,4],[9,7,8],[5,6,7]]
print(func(s,1000))