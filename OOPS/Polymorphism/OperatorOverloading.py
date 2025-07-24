# Operator Overloading - Python allows you to redefine the meaning of operators(+,-,/,//,*,% etc.) For user defined classes  this is form of compile time polymorphism.


# When we perform +,-,/,%,//,* etc. on a object of the class we can overload the operator using Magic method mathod 
# =================================
class Myclass:
    def __init__(self,para):
        self.para=para
    def __add__(self,other):
        return self.para+other.para
ob1=Myclass(100)
ob2=Myclass(200)
print(ob1+ob2)
# output: 300
# =================================

# ======================================
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages+other.pages
b=Book(100)
b1=Book(150)
print(b+b1)
# output: 250
# ======================================

# ======================================
class Compare:
    def __init__(self,para):
        self.para=para
    def __lt__(self,other):
        return self.para<other.para
C1=Compare(100)
C2=Compare(200)
print(C1<C2)
# output: True
# ======================================
        
# ======================================
class Comparision:
    def __init__(self,para):
        self.para=para
    def __le__(self,other):
        return self.para<=other.para
c1=Comparision(100)
c2=Comparision(100)
print(c1<=c2)  #100 c1 is equal to c2
# output: True  
# ======================================

# ======================================
class Counter:
    def __init__(self,count=10):
        self.count=count
    def __iadd__(self,other):
        self.count+=other
        return self
    def __str__(self):
        return str(self.count)
c=Counter()
c += 5
print(c)
# output:15
# ======================================