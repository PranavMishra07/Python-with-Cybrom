# Duck typing- "if it looks like a duck,swim like a duck and Quacks like a duck then it must be a duck."
# we dont need to check the type ,just call the method
# if an object has the methods or properties we except, we can use it -no matter what its actual class is.

#Enables Polymorphism without Inheritance- We  can write Function that work with any object, not just those from a particular heirarchy
# it makes our code more flexible, Concise,and polymorphic
class Duck:
    def quack(self):
        print("Quack !")
class Person:
    def quack(self):
        print("I am imitating a duck !")
def make_it_quack(thing):
    thing.quack()

# d=Duck()
# p=Person()

# make_it_quack(d)
# make_it_quack(p)

list=[Duck(),Person()]  #we can iterate class with this list 
for i in list:
    make_it_quack(i)







# -----------------------------------------------------------

class classA:
    def myfunction(self):
        print("This is class A")
class classB:
    def myfunction(self):
        print("This is class B")
class classC:
    def myfunction(self):
        print("This is class C")
def f(obj):
    obj.myfunction()

l=[classA(),classB(),classC()]
for i in l:
    f(i)
# ----------------------------------------------------------------------