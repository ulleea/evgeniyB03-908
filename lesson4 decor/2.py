def even_number(s):
    n=0
    for i in s:
        if i%2==0:
            n+=1
    return n


def change_even_number(even_number):
    def advanced_even_number(s):
        n=even_number(s)
        if n==0:
            print('Нет(')
        if n>10:
            print('Очень много')
    return advanced_even_number

s=input().split()
for i in range(len(s)):
    s[i]=int(s[i])
k=change_even_number(even_number)
k(s)

