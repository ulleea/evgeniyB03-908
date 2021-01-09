def simple(n=1,):
    global a
    while a:
        m = False
        k = 0
        for j in range(1, n + 1):
            if n % j == 0:
                if n == j or j == 1:
                        m = n
                else:
                    k = 1
        if k == 0:
            if m:
                print(m)
                thread2 = threading.Thread(target=stopper, args=())
                thread2.start()
                thread2.join(2.0)
        n+=1

def stopper():
    global a
    s=input()
    if s=='stop':
        a=False
        print(123)
    else:
        a=True
import threading
a=True
thread1=threading.Thread(target=simple,args=())
thread1.start()
