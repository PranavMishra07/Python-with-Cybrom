class myclass:
    def __init__(self,para):
        self.para=para
    def __gt__(self,other):
        return self.para>other.para
ob=myclass(287)
ob1=myclass(987)
print(ob>ob1)
