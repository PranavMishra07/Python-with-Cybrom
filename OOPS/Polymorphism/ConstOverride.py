# Constructor Override - CONStructor overriding occures when a child class provides its own __init__() method ,Which replaces(override) the __init__() method of the parent class 
# ==============================================
class mycls:
    def __init__(self):
        print("This is Default Constructor")
    def __init__(self,a):
        print("This is One argument constructor")
    def __init__(self,a,b,c):
        print("This is Three argument Constructor")
ob=mycls(12,4,5)
# output: This is Three argument Constructor

# in this class there are three constructor and the latest constructor override the previous constructors
# ==============================================


# ==============================================
# class Parent:
#     def __init__(self):
#         print("This is Parent Constructor")
# class Child(Parent):
#     def __init__(self):
#         print("This is Child Constructor")
# c=Child()
# outout : This is Child Constructor
# in this case the child class constructor override the parent class constructor
# ==============================================

# We can include parent class constructor to child class constructor using super() method
# ?======================================
class Parents:
    def __init__(self):
        print("Parent Constructor")
class Childs(Parents):
    def __init__(self):
        super().__init__()
        print("Child Constructor")
ob=Childs()
# output: Parent Constructor
#         Child Constructor
# ?======================================


# ?======================================
class Parents:
    def __init__(self):
        print("Parent Constructor")
class Childs(Parents):
    def __init__(self):
        super().__init__()
        print("Child Constructor")
ob=Childs()
# output: Parent Constructor
#         Child Constructor



