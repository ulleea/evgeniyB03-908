def neenumerate(iterable, start=0):
    _a=iterable
    _i=0
    while True:
        try:
            yield start,_a[_i]
            start+=1
            _i+=1
        except IndexError:
            break
arr=[1,2,3,4,5]
for i, a in neenumerate(arr):
    print(i,a)