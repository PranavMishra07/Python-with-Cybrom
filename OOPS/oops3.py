# class myclass:
#     def display(self):
#         print(f"HEllo display function is Calling{self}")
# obj=myclass
# obj.display("value")

# class myclass:
#     def display(self):
#         print("HEllo display function is Calling")
# obj=myclass()
# obj.display()
# kisi class ke function ke ander  self pass karte hai to
# class ka object banate samay parenthesis lagana padega


# class myclass:
#     def display(self,frm,lnm):  
#         print("HEllo display function is Calling",frm, lnm)# this is not best way
# obj=myclass()
# obj.display("Abc" , "Xyz")


# class myclass:
#     def display(self,frm,lmn):
#         self.frm=frm    
#         self.lmn=lmn  
#         print("HEllo display function is Calling",frm,lmn)
# obj=myclass()
# obj.display("abc","XYZ")
# wap to make calculator using self and return type with argument function input taken from user



# class myclass:
#     def display(self,frm,lmn):
#         self.frm=frm
#         self.lmn=lmn
#     def show(self):
#         print("deposit amount and acc No  : ",self.frm,self.lmn)
# obj=myclass()
# n1=int(input("Enter the No1 :"))
# n2=int(input("Enter the No2 :"))
# obj.display(n1,n2)
# obj.show()
# acc,pan,aadhar,deposit,withdraw


class Mybank:
    def ShowMenu(self,choose):
        print("Press 1 for Open Acount")
        print("Press 2 for Deposit Money")
        print("Press 3 for Withdraw Money")   
        self.choose=choose
        
        
    def userdata(self,name,aadhar,pan,account,amount):
        self.name=name
        self.aadhar=aadhar
        self.pan=pan
        self.account=account
        self.amount=amount
        
    def showdata(self):
        print(f"Name of User : {self.name}")
        print(f"Aadhar No is : {self.aadhar}")
        print(f"Pan No is : {self.pan}")
        print(f"Account No is : {self.account}")
        print(f"Amount in Bank : {self.amount}")
    def deposit(self,addmoney):
        self.addmoney=addmoney
        self.amount=self.amount+self.addmoney
        print(f"Deposit Amount : {self.addmoney}")
        print(f"Amount After Deposit : {self.amount}")
    def withdraw(self,takemoney):
        self.takemoney=takemoney
        withdr=self.amount-self.takemoney
        print(f"Amount after taking withdraw : {withdr}")


    

obj=Mybank()
choose=0
obj.ShowMenu(choose)
choose=int(input("Enter your Choice : "))

if(choose==1):
    name=input("Enter Your Name : ")
    aadhar=input("Enter your Aadhar No : ")
    pan=input("Enter Your Pan No : ")
    account=input("Enter Your Account No : ")
    amount=input("Enter the Amount you Want to deposit : ")
    obj.userdata(name,aadhar,pan,account,amount)
    obj.showdata()
    obj.ShowMenu(choose)
    
elif(choose==2):
    print("Enter The Amount You Want to Deposit")
    obj.deposit()   
elif(choose==3):
    obj.withdraw()

# obj.showdata()
# obj.deposit(5000)
<<<<<<< HEAD
# obj.withdraw(2000)
=======
# obj.withdraw(2000)
# Construtor are special type of function that gets call automatically when we create an object of a class in python we create an a constructor using __init__() 
>>>>>>> 201831275ccafe53f38a9d709c8c6b8a87473f4a
