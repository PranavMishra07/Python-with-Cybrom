
# wap to check number is palindrom or not 
# n=int(input("Enter any Number : "))
# res=0
# m=n
# while(n!=0):
#     r=n%10
#     res=res*10+r
#     n=n//10
# if(m==res):
#     print("Palindrom Number")
# else:
#     print("Not A palindrom Number")









    # user do value insert karega hame output first value ke bad second value tak ke palindrom No show karna hai 

n1=int(input("enter the No : "))
n2=int(input("No of palindrom you want: "))
i=1
n1+=1
while(i<=n2):
    temp=n1
    rev=0
    while(temp>0):
        r=temp%10
        rev=rev*10+r
        temp=temp//10
        if(rev==n1):
            print("Plindrom : ",rev)
            i+=1
    n1+=1