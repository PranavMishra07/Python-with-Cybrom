class myclass:
    def __init__(self,para):
        self.para=para
    def __gt__(self,other):
        return self.para>other.para
ob=myclass(297)
ob1=myclass(486)
print(ob>ob1)
