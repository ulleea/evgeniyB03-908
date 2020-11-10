class mother:

    def __init__(self,a):
        self.a=a

    def print(self):
        print('------')
        print(self.a)
        print('------')


class daughter(mother):

    def print(self):
        print(self.a)

a=mother(2)
b=daughter(4)
a.print()
print()
b.print()