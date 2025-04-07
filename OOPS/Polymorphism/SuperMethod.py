# Super Method- the super method used to call methods from a parent (superclass) to inside a Child class 
# its part of method overriding


class classA:
    def myfunction(self):
        print("This is class A")
class classB(classA):
    def myfunction(self):
        super().myfunction()
        print("This is class B")
class classC(classB):
    def myfunction(self):
        super().myfunction()
        print("This is class C")
ob=classC()
ob.myfunction()
# output : This is class A
#          This is class B
#          This is class C

# =========================================================
class myclass1:
    def __init__(self):
        print("This is Class 1 Constructor")
class myclass2(myclass1):
    def __init__(self):
        super().__init__()
        print("This is Class 2 Constructor")
ob=myclass2()
# ============================================================



