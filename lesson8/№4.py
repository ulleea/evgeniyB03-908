def func(s,n):
    from itertools import combinations_with_replacement
    a=[]
    for i in combinations_with_replacement(s, n):
        a.append(''.join(i))
    return sorted(a)
a='qwer'
print(func(a,2))