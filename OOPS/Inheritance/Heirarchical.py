# Hierarchical Inheritance where multiple derived class inherit from single Base class
#This allows the Base class Functionality to be shared among multiple derived class.

class BANK: #this class is inherited by two child classes 
    def RBIroi(self,amt):
        self.amt=amt
        self.ir=self.amt*12/100
        print("RBI ROI : ",self.ir)
class SBI(BANK):
    def SBIroi(self,amt):
        self.amt=amt
        self.ir=self.amt*7/100
        print("SBI ROI : ",self.ir)
class ICICI(BANK):
    def ICICIroi(self,amt):
        self.amt=amt
        self.ir=self.amt*10/100
        print("ICICI ROI : ",self.ir)
ob=ICICI()  #icici can access Bank class 
ob.ICICIroi(3535533)
ob.RBIroi(4205456)

obj=SBI()  # Sbi can also access Bank class 
obj.RBIroi(254354)
obj.SBIroi(13236)
