# wap to sum of digit input taken from user
count=0
t=(int(input("Enter Terms : ")))
while(count<t):
    n=int(input("Enter Any Number : "))
    rev=0
    while(n!=0):             
       r=n%10
       rev=rev+r
       n=n//10
    print(rev)
    count+=1