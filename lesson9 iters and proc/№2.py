
class Bintree:
    __s=0
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None
        self.prev=None
        self.start = None
        self.iter=0
        self.length=0
        self.last=False

    def get_value(self):
        return self.value

    def get_left(self):
        return self.__cur.left
    def get_right(self):
        return self.__cur.right
    def add(self,value2):
        self.__cur=self.start
        b=value2
        value2=Bintree(value2)
        if self.start is None:
            self.start = value2
            value2.prev=None
        else:
            a=self.__cur.get_value()
            c=1
            while c!=0:
                if a>b:
                    if self.__cur.left is None:
                        self.__cur.left=value2
                        value2.prev=self.__cur
                        c=0
                    else:
                        self.__cur=self.__cur.left
                else:
                    if self.__cur.right is None:
                        self.__cur.right=value2
                        value2.prev = self.__cur
                        self.__cur.last=False
                        self.__cur.right.last=True
                        c=0
                    else:
                        self.__cur=self.__cur.right

        self.length+=1
    def __len__(self):
        return self.length
    def __iter__(self):
        self.__cur=self.start
        return self
    def get_start(self):
        return self.start
    def set_start(self):

        return self
    def __next__(self):
        self.iter=1
        val=self.__cur.get_value()
        c=1
        while c!=0:
            if self.__s > 0:
                raise StopIteration()
            if self.__cur.left is None:
                if self.__cur.right is None:
                    if self.__cur.get_value()<self.__cur.prev.get_value():



                        while self.__cur.right is None:
                            if self.__cur.prev == None:
                                raise StopIteration()
                            self.__cur=self.__cur.prev
                        if self.__cur.right!= None:
                            self.__cur=self.__cur.right
                            c=0
                    else:
                        while self.__cur.right is None:
                            if self.__cur.last==True:
                                self.__s+=1
                            for j in range(3):
                                if self.__cur.prev == None:
                                    raise StopIteration()
                                self.__cur=self.__cur.prev
                        if self.__cur.right!= None:
                            self.__cur=self.__cur.right
                            c=0

                else:
                    self.__cur=self.__cur.right
                    c=0
            else:
                self.__cur=self.__cur.left
                c=0
        return val
a=Bintree()
for i in range(10):
    a.add(i)
z=a.get_start()
# for i in range(10):
#     print(z.get_value(),z.last)
#     z=z.right
print(a.get_start().right.get_value())
print(len(a))
print()
for i in a:
    print(i)