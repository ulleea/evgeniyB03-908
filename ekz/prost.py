def simple(n):
    for i in range(1,n+1):
        m=False
        k=0
        for j in range(1,i+1):
            if i%j ==0:
                if i==j or j==1:
                    m=i
                else:
                    k=1
        if k==0:
            if m :
                yield m
    if m==False:
        print('end')



n=10
for i in simple(n):
    print(i)