import time
import threading
def summ(i):
    with lock:
        global s1
        s1+=a[i]
n=10
for j in range(0,10,2):
    n+=j
    a=[]
    s1=0
    lock = threading.Lock()
    for i in range(n):
        a.append(i)
    s=0
    start = time.time()
    for i in a:
        s+=i
    t=time.time()-start
    start1=time.time()
    threads = [threading.Thread(target=summ, args=(i,)) for i in range(0, n)]
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    t1=time.time()-start1
    print('@',s,s1,'@',t,t1,'@',n)
