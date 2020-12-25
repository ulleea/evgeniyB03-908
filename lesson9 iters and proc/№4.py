def coroutine():
    print('start')
    s=0
    n=0
    try:
        while True:
            a=yield
            s+=a
            n+=1
            print((s/n),abs(a-s/n),n)
            yield (s/n),abs(a-s/n),n
    finally:
        print("Stop coroutine")
coroutine=coroutine()
s=input()
if s=='False':
    print('end')
else:
    s=int(s)
    next(coroutine)
    while s:
        a,b,c=coroutine.send(s)
        print(a,b,c)
        next(coroutine)
        s=input()
        if s == 'False':
            break
        else:
            s=int(s)
