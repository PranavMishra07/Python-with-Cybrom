# write a program to find all the prime number between two user input,also the number which have exactly 4 factor and show the factor
# n=int(input("enter Any Number : "))
# i=1
# count=0
# for i in range(1,n+1,+1):
#     if(i%2==0):
#         fact=i
#         print("Factors are : ",fact)        
#         count+=1
# if(count==2):
#     print("prime")
# else:
#     print("Not Prime")

n1=int(input("enter first Number : "))
n2=int(input("Enter Second Number : "))
if(n1>0):
    for i in range(n1,n2+1):
        cnt=0
        for j in range(1,i+1):
            if(i%j==0):
                cnt+=1
        if(cnt==2):
            print("Prime : ",i)
        elif(cnt==4):
            print("four Factor : ",i)