# n=(int(input("Enter a Number : ")))
# cnt=0
# i=1
# while(i<=n):
#     if(n%i==0):
#         cnt+=1
#     i+=1                #if ke bahar
# if(cnt==2):              #While ke bahar
#     print("Prime")
# else:
#     print("Not Prime")


# 2nd way

# n=(int(input("Enter a Number : ")))
# cnt=0
# i=2
# while(i<n):
#     if(n%i==0):
#         cnt+=1
#     i+=1                #if ke bahar
# if(cnt==0):              #While ke bahar
#     print("Prime")
# else:
#     print("Not Prime")


n=(int(input("Enter a Number : ")))
cnt=0
i=1
while(i<=n//2):
    if(n%i==0):
        cnt+=1
    i+=1                #if ke bahar
if(cnt==2):              #While ke bahar
    print("Prime")
else:
    print("Not Prime")


