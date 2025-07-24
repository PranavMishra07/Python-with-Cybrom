class myclass:
    def __init__(self,para):
        self.para=para
    def __gt__(self,other):
        return self.para>other.para
ob=myclass(300)
ob1=myclass(100)
print(ob>ob1)
print(ob<ob1)


