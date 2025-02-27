#python is a high level ,object oriented ,open source ,interpreted,syntexless,indentloosed,generalpurpose,platform-independent,Dynamic Memory allocation and easy to learn Language
# print("hello World!")
# print(2+2)
# print(2*4)
# a=23
# print(id(a))
# print(type(a))
# a=20
# print(id(a))
# print(a)
# a=2.2
# print(type(a))
# print(a*a)
# a=5
# a+=2
# print(a)
# write a program to swap two variable without using third variable and without using arithmetic opration
a=int(input("Enter The First No : "))
b=int(input("Enter The Second No : "))
print(f"Before Swapping The value of a={a} and b={b}")   #fstring -formating string
a,b=b,a
print(f"After Swapping The value of a={a} and b={b}")   #fstring -formating string
num1=5
num2=6
print(f"Before Swapping the value of Num1 ={num1} and Num2 ={num2}")
num1=num2
num3=num2
num3=num1
print(f"After Swapping the Value of Num1={num1} and Num2={num2}")