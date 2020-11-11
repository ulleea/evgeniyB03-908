def nezip(*a):
    _a=list(a)
    m=0
    for i in _a:
        if len(i)>m:
            m=len(i)
    _q=0
    while True:
        _b=[]
        try:
            for i in _a:
                _b.append(i[_q])
            _q+=1
            yield tuple(_b)
        except IndexError:
            break
a=[1,2,3,4,5]
b=[2,3,4,5]
c=[9,8,7,6,5]
for i in nezip(a,b,c):
    print(i)
