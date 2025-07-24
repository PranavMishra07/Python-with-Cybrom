# A subclass provide a specific implementation of a method that is already defined in its superclass .
# Method ovverriding happens when a child class defines a method with the same name as a method in the parent class the childs version replaces the parents version when called on an instance of the child class.
# ==============================

class classA:
    def myfunction(self):
        print("This is class A")
class classB(classA):
    def myfunction(self):
        print("This is class B")
class classC(classB):
    def myfunction(self):
        print("This is class C")
ob=classC()
ob.myfunction()
# output: This is class C

# ==============================
# ==============================
class Animals:
    def speak(self):
        return "Animal Sound"
class Dog(Animals):
    def speak(self):
        return "Woof !"
class Cat(Animals):
    def speak(self):
        return "Meow !"
    
# animal=[Dog(),Cat()]
# for a in animal:
#     print(a.speak())
# output:Woof !
#        Meow !



animal1=Dog()
print(animal1.speak())
# output: Woof !

animal2=Cat()
print(animal2.speak())
# output: Meow !

# this is example of heirarchical inheritance where Dog and Cat child classes inherit from the Parent Animals class
# in this case the parent class speak method is overridden by the child class speak method
# ==============================

# ==============================
class Parent :
    def greet(self):
        print("Hello from Parent")
class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child")
ob= Child()
ob.greet()
# output : Hellow from Parent
#          Hello from Child
# ==============================
# ==============================
class BankAccount:
    def interest_rate(self):
        return "5%"
class PremiumAccount(BankAccount):
    def interest_rate(self):
        return "7%"
acc1=BankAccount()
acc2=PremiumAccount()

print(acc1.interest_rate())  #output: 5%  Parent class interest_rate
print(acc2.interest_rate())  #output: 7%  Premium account override the Bankaccounts interest_rate
# ==============================
# ==============================
class Shape:
    def area(self):
        return 0       
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
c=Circle(5)
print(f"Area Of a Circle is : {c.area()} ")
# output: Area Of a Circle is : 78.5
# ==============================

class Logger:
    def log(self,msg):
        print(f"LOG : {msg} ")
class TimestampLogger(Logger):
    def log(self,msg):
        import datetime
        super().log(f"{datetime.datetime.now()}:{msg}")
logger=TimestampLogger()
logger.log("System Started")
# output: LOG : 2025-04-07 17:35:50.463991:System Started
# ====================================
