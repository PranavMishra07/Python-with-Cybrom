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


# def noreturn_noargument():
#     a=10
#     b=20
#     c=a+b
#     print("Addition : ",c)
# noreturn_noargument()


# when user pass the value in the parertheses while calling the function is called argument

# paramenter is a variable to accept argument from the user



# No return with argument
# def noreturnwithargument(n):
#     for i in range(1,n+1,1):
#         for j in range(1,i+1,1):
#             print(j,end=" ")
#         print()
# noreturnwithargument(5)

# def noreturnwithargument(n):
#     for i in range(1,n+1,1):
#         for j in range(1,i+1,1):
#             print(i,end=" ")
#         print()
# noreturnwithargument(5)



# def noreturnwithargument(n):
#     for i in range(n,0,-1):
#         for j in range(1,i+1,1):
#             print(i,end=" ")
#         print()
# noreturnwithargument(5)

# def noreturnwithargument(n):
#     for i in range(n,0,-1):
#         for j in range(1,i+1,1):
#             print(j,end=" ")
#         print()
# noreturnwithargument(5)


# def noreturnwithargument(n=10):
#     for i in range(n,0,-1):
#         for j in range(1,i+1,1):
#             print(j,end=" ")
#         print()
# noreturnwithargument()



# def noreturnwithargument(n=10):
#     for i in range(n,0,-1):
#         for j in range(1,i+1,1):
#             print(i,end=" ")
#         print()
# noreturnwithargument()


# hello=noreturnwithargument
# hello()



# def return_noargument():
#     a=10
#     b=20
#     c=a+b
#     d=a*b
#     return c,d
# x=return_noargument()
# add=0
# for i in x:
#     add = add+i
# print(add)


# def return_noargument():
#     a=10
#     b=20
#     c=a+b
#     d=a*b
#     return c,d
# x=return_noargument()
# # add=x[0]+x[1]
# # print(add)
# add=0
# for i in x:
#     add = add+i
# print(add)

def return_withargument(a,b):
    c=a+b
    d=a*b
    return c,d
x=return_withargument(10,20)
add=0
for i in x:
    add=add+i
print(add)
# wap using function with all four type also use while loop and for loop to make a choice based of 20 program
# in which ten are from pattern and ten are from arstrong strong palindrom reverse 
# note user can exit from the program only press 21


# types of argument
# keyword argument default argument arbitrory argument