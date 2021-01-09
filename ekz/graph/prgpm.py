def graph(s,l):
    d=dict()
    with open(s,'r') as file:
        for a in file:
            a=a.split()
            q=len(a)
            d[int(a[0])]=[]
            for i in range(1,q):
                d[int(a[0])].append(int(a[i]))
    for i in range(l):
        for k in range(reb):
            if d[i][k]==1:
                for j in range(l):
                    if i==j:
                        pass
                    else:
                        if d[j][k]==-1:
                            g[i].add(j)
def glub(s):
    l=0
    reb=0
    with open(s, 'r') as file:
        for i in file:
            l+=1
            reb=len(i.split())-1
    for i in range(l):
        g[i]=set()
    return l,reb

def groups(s):
    with open(s, 'r') as file:
        r=0
        for str in file:
            str=str.split()
            q=len(str)
            gr[int(str[0][:-1])]=set()
            for i in range(1,q):
                if i!=q-1:
                    gr[int(str[0][:-1])].add(int(str[i][:-1]))
                else:
                    gr[int(str[0][:-1])].add(int(str[i]))

def count(gr,i,g):
    sum=0
    for  j in gr[i]:
        for u in g[j]:
            if u in gr[i]:
                sum+=1
    return sum
def group_rand(a,ln,i,g,l):
    import random
    a[i]=set()
    t=0
    while t!=ln:
        q=random.randint(0,l-1)
        if q in a:
            pass
        else:
            a[i].add(q)
            t+=1
def paral(gr,i,g,l):
    ln = len(gr[i])
    a = dict()
    group_rand(a, ln, i, g, l)
    t=count(a, i, g)
    return t
from multiprocessing import Process,Lock
from multiprocessing import Pool
if __name__ == '__main__':

    lock = Lock()
    g=dict()
    gr=dict()
    s1='C:\\Users\\Евгений\\PycharmProjects\\pycharmrepository\\repositoriy\\ekz\\graph\\1.txt'
    s2='C:\\Users\\Евгений\\PycharmProjects\\pycharmrepository\\repositoriy\\ekz\\graph\\2.txt'
    n=4
    pool=Pool(processes=n)
    l,reb=glub(s1)
    graph(s1,l)
    groups(s2)
    m=len(gr)
    import time
    print(g)
    print(gr)
    o=time.time()
    threads = [pool.apply(count,args=(gr,i,g,)) for i in range(m)]

    threadsrand=[]
    for i in range(100):
        y=[pool.apply(paral,args=(gr,i,g,l,)) for i in range(m)]
        threadsrand.append(y)


    sr=[0 for i in range(5)]
    print(sr)
    for j in range(5):
        for i in range(100):
            sr[j]+=threadsrand[i][j]
        sr[j]=sr[j]/100
    print(sr)
    print(threads)
    o2=time.time()
    print(o2-o)

