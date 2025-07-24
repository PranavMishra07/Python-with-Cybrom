# when more than one class can be inherits by a single another class this concept is known as Multiple inheritance 
class SBI:
    def SBIroi(self,amt):
        self.amt=amt
        self.ir=self.amt*7.8/100
        print("SBI ROI = ",self.ir)
class ICICI:
    def ICICIroi(self,amt):
        self.amt=amt
        self.ir=self.amt*9.2/100
        print("ICICI ROI : ",self.ir)
class HDFC:
    def HDFCroi(self,amt):
        self.amt=amt
        self.ir=self.amt*12/100
        print("HDFC ROI : ",self.ir)
class BANKS(SBI,ICICI,HDFC): #Banks inherits all three its parent class (SBI,ICICI,HDFC)
    pass  #To avoid syntax errors when the structure is necessary but logic isn’t written yet.
obj=BANKS()  # this object can access all methods from his parents
# obj.SBIroi(1000)
# obj.ICICIroi(5000)
# obj.HDFCroi(65000)
amount=int(input("Enter The Amount : "))
obj.SBIroi(amount)
obj.ICICIroi(amount)
obj.HDFCroi(amount)
