def simple():
    global a,n
    if a:
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
        n+=1

def stopper():
    global a
    s=input()
    if s=='stop':
        a=False
    else:
        a=True

def runner():
    while a:
        thread1 = threading.Thread(target=simple, args=())
        thread1.start()
        thread1.join()

        thread2 = threading.Thread(target=stopper, args=())
        thread2.start()
        thread2.join(2.0)
import threading
a=True
n=1
runner()
print('end')

