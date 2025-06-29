# a=10
# b=3
# c=a+b
# print(c)
# c=a-b
# print(c)
# c=a*b
# print(c)
# c=a/b
# print(c)
# c=a//b
# print(c)
# c=a%b
# print(c)
#relational operation always return boolean Value there are 6 

a=int(input("Enter First Number : "))
b=int(input("Enter second Number : "))
c=int(input("Enter third Number : "))
d=int(input("Enter Fourth Number : "))
max=a
if b>max :
   max=b 
if c>max :
   max=c   
if d>max :
 max=d
print(f"Maximum Number is :{max}")
