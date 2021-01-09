class Graph:
    def __init__(self,s1,s2,n):
        self.g=dict()
        self.gr = dict()
        self.d = dict()
        self.s1=s1
        self.s2=s2
        self.l=0
        self.reb=0
        self.a=dict()
        self.n=n
        self.threads=[]
        self.m=0
    def graph(self):
        with open(self.s1,'r') as file:
            for a in file:
                a=a.split()
                q=len(a)
                self.d[int(a[0])]=[]
                for i in range(1,q):
                    self.d[int(a[0])].append(int(a[i]))
        for i in range(self.l):
            for k in range(self.reb):
                if self.d[i][k]==1:
                    for j in range(self.l):
                        if i==j:
                            pass
                        else:
                            if self.d[j][k]==-1:
                                self.g[i].add(j)

    def glub(self):
        l=0
        reb=0
        with open(self.s1 , 'r') as file:
            for i in file:
                l+=1
                reb=len(i.split())-1
        for i in range(l):
            self.g[i]=set()
        self.l=l
        self.reb=reb

    def groups(self):
        with open(self.s2, 'r') as file:
            for str in file:
                str=str.split()
                q=len(str)
                self.gr[int(str[0][:-1])]=set()
                for i in range(1,q):
                    if i!=q-1:
                        self.gr[int(str[0][:-1])].add(int(str[i][:-1]))
                    else:
                        self.gr[int(str[0][:-1])].add(int(str[i]))

    def get_grp(self):
        self.m=len(self.gr)
        return self.m

    def count(self,i):
        sum=0
        for  j in self.gr[i]:
            for u in self.g[j]:
                if u in self.gr[i]:
                    sum+=1
        return sum

    def group_rand(self,ln,i):
        import random
        self.a[i]=set()
        t=0
        while t!=ln:
            q=random.randint(0,self.l-1)
            if q in self.a:
                pass
            else:
                self.a[i].add(q)
                t+=1
    def paral(self,i):
        ln = len(self.gr[i])
        self.group_rand( ln, i)
        t=self.count( i)
        return t

    def pros(self):
        self.glub()
        self.graph()
        self.groups()
        self.get_grp()
        from multiprocessing import Pool
        pool = Pool(processes=self.n)
        self.threads = [pool.apply(self.count, args=(i,)) for i in range(self.m)]
        self.threadsrand = []
        for i in range(1000):
            y = [pool.apply(self.paral, args=(i,)) for i in range(self.m)]
            self.threadsrand.append(y)
        return self.threads, self.threadsrand

from multiprocessing import Process,Lock
from multiprocessing import Pool
if __name__ == '__main__':

    s1='C:\\Users\\Евгений\\PycharmProjects\\pycharmrepository\\repositoriy\\ekz\\graph\\1.txt'
    s2='C:\\Users\\Евгений\\PycharmProjects\\pycharmrepository\\repositoriy\\ekz\\graph\\2.txt'
    # n=1
    # pool=Pool(processes=n)
    # g=dict()
    # gr=dict()
    # l,reb=glub(s1)
    # graph(s1,l)
    # groups(s2)
    # m=len(gr)
    # print(g)
    # print(gr)
    import time
    o=time.time()
    w=Graph(s1,s2,1)
    # threads = [pool.apply(count,args=(gr,i,g,)) for i in range(m)]
    #
    # threadsrand=[]
    # for i in range(1000):
    #     y=[pool.apply(paral,args=(gr,i,g,l,)) for i in range(m)]
    #     threadsrand.append(y)
    threads,threadsrand=w.pros()
    print(threads)
    print(threadsrand)
    sr=[0 for i in range(16)]
    for j in range(16):
        for i in range(1000):
            sr[j]+=threadsrand[i][j]
        sr[j]=sr[j]/1000
    print(sr)
    print(threads)
    o2=time.time()
    print(o2-o)