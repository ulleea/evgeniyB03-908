def fibonachi(n):
    if n==1 or n==2:
        return 1
    _a1=0
    _a2=1
    _i=1
    while True:
        yield _a2
        _a1,_a2=_a2,_a2+_a1
        if _i==n:
            break
        _i+=1


n=int(input())
for i in fibonachi(n):
    print(i)