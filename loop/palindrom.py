
# wap to check number is palindrom or not 
n=int(input("Enter any Number : "))
res=0
m=n
while(n!=0):
    r=n%10
    res=res*10+r
    n=n//10
if(m==res):
    print("Palindrom Number")
else:
    print("Not A palindrom Number")