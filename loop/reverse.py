# wap to reverce the input digit input taken from user
n=int(input("Enter any Number : "))
res=0
m=n
while(n!=0):
    r=n%10
    res=res*10+r
    n=n//10
print("Reverse",res)