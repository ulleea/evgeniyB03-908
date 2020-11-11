def func(a,b):
    from itertools import product
    return list(product(a,b))
a=[1,2,3]
b=(9,8,7)
print(func(a,b))