def graph(s,l):
    with open(s,'r') as file:
        for a in file:
            a=a.split()
            q=len(a)
            d[int(a[0])]=[]
            for i in range(1,q):
                d[int(a[0])].append(int(a[i]))
    for i in range(l):
        for k in range(q):
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

def count(gr,i):
    sum=0
    for  j in gr[i]:
        sum+=len(g[j])
    d[i].append(sum)

def group_rand(a,ln):
    import random
    a[i]=set()
    t=0
    while t!=ln:
        q=random.randint(1,l)
        if q in a:
            pass
        else:
            a[i].add(q)
            t+=1


def paral(gr,i):
    with lock:
        count(gr,i)
        ln=len(gr[i])
        for j in range(3):
            a=dict()
            group_rand(a,ln)
            count(a,i)
        sr=0
        for k in range(len(d[i])):
            sr+=d[i][k]
        d[i].append(sr/len(d[i]))

import threading
lock = threading.Lock()
d=dict()
g=dict()
gr=dict()
s1=input()
s2=input()
n=int(input())

l,reb=glub(s1)
graph(s1,l)
m=len(gr)
d=dict()
for i in range(m):
    d[i]=[]
threads = [threading.Thread(target=count,args=(gr,_)) for _ in range(m)]
for i in threads:
    i.start()

for i in range(len(d)):
    print(d[i])

# g=dict()
# for i in  range(10):
#     g[i]=10-i
# g[10]=1
# for i in range(10):
#     print(g[i])
# print(len(g))
# a=set()
# s='1, 2, 3, 34, 56'
# s=s.split()
# a.add(int(s[0][:-1]))
# print(s[4])
