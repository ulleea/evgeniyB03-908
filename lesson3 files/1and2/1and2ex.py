def rewrite ():
    with open('G:\\python\\pycharm projects\\files\\text.txt','r') as file:
        q=file.read()
        print(q)
        print(type(q))
    with open('G:\\python\\pycharm projects\\files\\text.txt','w') as output:
        q=q.split()
        print(q)
        s=q[0]
        for i in range(1,len(q)):
            s+=' '+q[i]
        output.write(s)
        print('-------------------')
    pass
def writearray(arr):
    with open('G:\\python\\pycharm projects\\files\\1ext.txt','w') as file:
        arr = map(lambda x: x + '\n', arr)
        file.writelines(arr)

arr=['qwe','rty','uio']
rewrite()
writearray(arr)
