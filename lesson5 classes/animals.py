class animals :
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def description(self):
        print(self.name,self.age,self.kind )


class zebra(animals):
    kind='zebra'


class dolphin(animals):
    kind='dolphin'

a=zebra('bob',12)
b=dolphin('martha',14)
a.description()
print('---------')
b.description()