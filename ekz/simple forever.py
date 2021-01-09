def simple():
    n=1
    while True:
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
                yield m
        n+=1

for i in simple():
    print(i)
