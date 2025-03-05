# when we declare more than one loop inside another loop that type of condition is called nested loop
# initialization of outer loop
# while(condition):
    # initialization of inner loop
    # while(condition):
        # inc/dec of innerloop
    # inc/dec of outerloop
# i=1
# while(i<=4):
#     print("Outer Loop Chala",i)
#     j=1
#     while(j<=5):
#         print("Inner Loop Chala ",j,end=" ")
#         j+=1
#     i+=1


# n1=int(input("enter the No : "))
# n2=int(input("No of palindrom you want: "))
# i=1
# n1+=1
# while(i<=n2):
#     temp=n1
#     rev=0
#     while(temp>0):
#         r=temp%10
#         rev=rev*10+r
#         temp=temp//10
#         if(rev==n1):
#             print("Plindrom : ",rev)
#             i+=1
#     n1+=1

    # wap using choice besed user can exit from the program only if user can press 5 
# continue loop ko repeat
# pass current loop ko khatam or next loop par jump
#eval= evaluate from string and 



while(True):                                   #loop start
    n=int(input("enter number : "))            #input taken
    if(n==1):                                  #condition
        print("Press 1")                       #print
    elif(n==2):                                
        print("press 2")
    elif(n==3):
        print("Press 3")
    elif(n==4):
        print("out of the loop")
        pass    
    while(True):
        print("Press 1 For addition")
        m=int(input("Enter Number : "))              #break the loop end exit 
        if(m==1):
            a= eval(print("Enter First Number : "))
            b= eval(input("Enter Second Number : "))
           
            
            print(f"Addition of {a} and {b} = {a+b}")            
            break
        
