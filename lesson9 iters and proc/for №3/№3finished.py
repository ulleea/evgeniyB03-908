class TextLoader:
    def __init__(self,path,str=None):
        self.path=path
        self.len=0
        import os
        os.chdir(self.path)
        self.list=os.listdir(self.path)
        self.start=self.list[0]
        self.str=str
        self.last=False

    def get_idx(self):
        n=-1
        for i in range(self.len):
            if self.__cur==self.list[i]:
                n=i
                break
        return n

    def c_reg(self):
        import  os
        st=''
        if not self.str.endswith('.txt'):
            os.rename(self.path+'\\'+self.str,self.path+'\\'+ self.str+'.txt')
        __s=''
        __a = [ord('а'), ord('я'), ord('a'), ord('z'), ord('0'), ord('9')]
        with open(self.path + '\\' +self.str, 'r', encoding='utf-8') as reader:
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
                st = st +__s + '\n'
        with open(self.path + '\\' +self.str, 'w', encoding='utf-8') as writer:
            writer.write(st)
        return st

    def __len__(self):
        import os
        os.chdir(self.path)
        self.len=len(self.list)
        return self.len

    def __iter__(self):
        self.__cur=self.start
        return self

    def __getitem__(self, item):
        if item>= self.len:
            raise IndexError("Index out of range")
        c=TextLoader(self.path,self.list[item])
        return c.c_reg()

    def __next__(self):
        if self.get_idx()==-1:
            raise StopIteration
        n=self.get_idx()
        val =self.__getitem__(n)
        if n+1<self.len:
            self.__cur=self.list[n+1]
        else:
            self.len=-1
        return val