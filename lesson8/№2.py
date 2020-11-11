def func(s,n):
    from itertools import permutations
    a=[]
    for i in permutations(s, n):
        a.append(''.join(i))
    return sorted(a)
a='qwer'
print(func(a,2))