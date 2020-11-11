def func(s):
    from itertools import groupby
    a=[]
    for k, g in groupby(s):
        b=list(g)
        c=(*b[0],len(b))
        a.append(c)
    return print(a)
s='1111222334'
func(s)


