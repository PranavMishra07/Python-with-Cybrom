#control structure statement (Loop)
#there are only two types of loop in python  While and For loop
#deference between for and while
#syntex of while loop
#1- initialization 
# 2-Condition
# 3-increment / decrement iterator
#write a program to add ten natural Number
# i=1
# add_natural_number=0
# while(i<=10):
#     add_natural_number=add_natural_number+i
#     i+=1
# print("Addition",add_natural_number)

num=int(input("Enter Num"))
even=0
odd=0
i=1
while(i<=num):
    if(i%2==0):
       even=even+i
    else:
       odd=odd+i   
    i+=i         
print("Even Num",even)
print("Odd Num",odd)
# wap to find the 1,-2 +3 -4 +5 ...input taken from user
# find the sum of factorial 1-factorial 2 + factorial 3 -....input taken from user
# find the number of factor of any number input taken from user also show the factor
wap to check the number is prime or not in different ways taken from user
# wap to check number is armstrong or not 
