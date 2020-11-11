def func(s,n):
    from itertools import permutations
    a=[]
    for j in range(1,n+1):
        r=[]
        for i in permutations(s, j):
            r.append(''.join(i))
        r=sorted(r)
        a.extend(r)
    return a
a='qwer'
print(func(a,2))