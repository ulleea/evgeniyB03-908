# # os.chdir('C:\\Users\\Евгений\\.PyCharmCE2019.3\\config\\scratches\\pythonreposit\\lesson9 iters and proc\\for №3\\sample')

class TextLoader:
    def __init__(self,path,str=None):
        self.path=path
        self.len=0
        import os
        os.chdir(self.path)
        self.list=os.listdir(self.path)
        self.start=self.list[0]
        self.str=str
    def get_str(self,item):
        return self.list[item]
    def c_reg(self,str):
        import  os
        if not self.__cur.endswith('.txt'):
            os.rename(self.path+'\\'+self.__cur,self.path+'\\'+ self.__cur+'.txt')
        __s=''
        __a = [ord('а'), ord('я'), ord('a'), ord('z'), ord('0'), ord('9')]
        with open(self.path + '\\' +self.__cur, 'r', encoding='utf-8') as reader:
            __a = [ord('а'), ord('я'), ord('a'), ord('z'), ord('0'), ord('9')]
            for i in reader:
                __s = i.lower()
                __s = __s[0:-2]
                j = 0
                while j < len(__s):
                    if (ord(__s[j]) >= __a[0] and ord(__s[j]) <= __a[1]) or ord(__s[j]) == ord(' '):
                        pass
                    else:
                        __s = __s[0:j] + __s[j + 1::]
                        j -= 1
                    j += 1
                __s = __s + '\n'
                print(__s)
    def __len__(self):
        import os
        os.chdir(self.path)
        self.len=len(os.listdir(os.getcwd()))
        return self.len
    def __iter__(self):
        self.__cur=self.start
        return self
    def __getitem__(self, item):
        if item>= self.len:
            raise IndexError("Index out of range")
        return self.list[item].c_reg()
class Ch_reg(TextLoader):
    def __init__(self):
        self.str=str
# import os
# os.chdir('C:\\Users\\Евгений\\.PyCharmCE2019.3\\config\\scratches\\pythonreposit\\lesson9 iters and proc\\for №3\\sample')
# a=os.listdir('C:\\Users\\Евгений\\.PyCharmCE2019.3\\config\\scratches\\pythonreposit\\lesson9 iters and proc\\for №3\\sample')
#
# c='C:\\Users\\Евгений\\.PyCharmCE2019.3\\config\\scratches\\pythonreposit\\lesson9 iters and proc\\for №3\\sample'+'\\'+a[0]
# if c.endswith('.txt'):
#     pass
# else:
#     os.rename('C:\\Users\\Евгений\\.PyCharmCE2019.3\\config\\scratches\\pythonreposit\\lesson9 iters and proc\\for №3\\sample'+'\\'+a[0],'C:\\Users\\Евгений\\.PyCharmCE2019.3\\config\\scratches\\pythonreposit\\lesson9 iters and proc\\for №3\\sample'+'\\'+a[0]+'.txt')
# a=os.listdir('C:\\Users\\Евгений\\.PyCharmCE2019.3\\config\\scratches\\pythonreposit\\lesson9 iters and proc\\for №3\\sample')
# k=0
# with open('C:\\Users\\Евгений\\.PyCharmCE2019.3\\config\\scratches\\pythonreposit\\lesson9 iters and proc\\for №3\\sample'+'\\'+a[0] ,'r',encoding='utf-8') as reader:
#     __a = [ord('а'), ord('я'), ord('a'), ord('z'), ord('0'), ord('9')]
#     print(__a,ord(' '))
#     # __a=[',','-','.','!','?',';',]
#     print('C:\\Users\\Евгений\\.PyCharmCE2019.3\\config\\scratches\\pythonreposit\\lesson9 iters and proc\\for №3\\sample'+'\\'+a[0])
#     for i in reader:
#         k+=1
#         __s=i.lower()
#         __s=__s[0:-2]
#         j=0
#
#         while j<len(__s):
#             if (ord(__s[j])>=__a[0] and ord(__s[j])<=__a[1]) or ord(__s[j])==ord(' '):
#                 pass
#             else:
#                 __s=__s[0:j]+__s[j+1::]
#                 j-=1
#             j+=1
#         __s=__s+'\n'