# Construtor are special type of function that gets call automatically when we create an object of a class in python we create an a constructor using __init__() 
# the main purpose of a constructor is to initialize or asign values to the data member of that class. it cannot return any value other than none. when constructor called they initialize a memory
# when the constructor doesn't accept any argument from the object and has only one argument self in the constructor it isknown as default constructor
# this is default Constructor-
class myclass:
    def __init__(self):
        print("HEllo World")
ob= myclass()
# Parameterized Constructor accepts arguments along with self it is known as parameterized constructor
class mycons:
    def __init__(self,fnm,snm):
        self.fnm=fnm
        self.snm=snm
obj=mycons("Pranav" ,"Mishra")
print(obj.fnm,obj.snm)

# A destructor= is a special type of function /Method used to clean up resources when an object is deleted or goes out of scope
# it is defined using __del__() it is automatically called when an object release a memory or an object is no longer refferenced



class myclass:
    def __init__(self):
        print("this is default constructor ")
    def __init__(self,a):
        print("This is one argument Constructor")
    def __init__(self,a,b,c):
        print("This is third Constructor")
ob=myclass(10,20,30)