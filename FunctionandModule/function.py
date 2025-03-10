# Function Modules
# kisi ek file ke andar bahut sare function ho 
# a file containing multiple functions that particular file known as Module
# function is a block of code when we want to reuse we call the function
# Types of function
# 1 predefine function  -- already defined ex: int,input,pre
# 2 User define functions-- user can declare function in four ways -->
#1= No return No argument
#2= no return with argument
#3= return without argument
#4= return with argument

# in python one more single line function which is anonymous function named lamda functions
# in python thre more function which is map(),filter(),reduce()


# Local and global variable
# when we declare any variable inside the function then scope of this variable are only present inside the function
# when we declare any variable outside the function then scope of this variable are outside the function as well as inside the function


# Sytex of a function
# def is reserved keyword
# in function block there is statements and code
# def function_name():   defining the function
#     statement 1        statements
#     statement 2

# function_name()        call the function


def noreturn_noargument():
    a=10
    b=20
    c=a+b
    print("Addition : ",c)
noreturn_noargument()


# when user pass the value in the parertheses while calling the function is called argument

# paramenter is a variable to accept argument from the user
