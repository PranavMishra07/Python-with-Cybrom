# find factorial of any number input taken from user
# find sum of factorial 1 + factorial 2 + factorial 3.. input taken from user

n1=int(input("Enter any Number : "))
fact1=1
i=1
while(i<=n1):
    fact1=fact1*i   
    i+=1 
print("factorial 1 :",fact1)

n2=int(input("Enter any Number : "))
fact2=1
i=1
while(i<=n2):
    fact2=fact2*i   
    i+=1 
print("factorial 2 :",fact2)

n3=int(input("Enter any Number : "))
fact3=1
i=1
while(i<=n3):
    fact3=fact3*i   
    i+=1 
print("factorial 3 :",fact3)


print("Sum of Three factorial",fact1+fact2+fact3)