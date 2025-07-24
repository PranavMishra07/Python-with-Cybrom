#Inheritance is a ability to take/inherit properties and Features of an class to another class

#when a class derives from another class the child class will inherit all the public and protected properties and methods from the parent class in addition it can have its own properties and methods, this is called as inheritance.

# Types of Inheritance:
# Single Inheritance
# Multiple Inheritance
# Multilevel Inheritance
# Heirarchical Inheritance


# Base class- A base class(Parent,Superclass) is a class that can provides Comman attributes and Methods that can be Inherited by other class.
# Derived Class - A Derived Class(Child,Subclass) is a class that Inherits from the Base Class and can extend or Override its functionality.

# Single Inheritance: A derived class inherits from a single Base class.
# A Derived class must have only one parent class and a Parent class must have only one derived class then such type of inheritance is called single Inheritance.
class myclassA:
    def classA(self):
        print("Parent Class Function")
class MyclassB(myclassA):
    def classB(self):
        print("Child Class Function")
obj=MyclassB()  # object of child class
obj.classA()  #Accessing Parent class through the child class
obj.classB()



class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showDetails(self):
        print(f"The name of Employee {self.id} is {self.name} ")
class Programmer(Employee):
    def showLanguage(self):
        print("The Default Language is Python")
emp=Employee("Pranav",1)
emp.showDetails()

emp2=Programmer("Himanshu",2)
emp2.showDetails()
emp2.showLanguage()



