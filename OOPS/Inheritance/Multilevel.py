# in Multilevel the the one class can be inherited by another class further this class also inherited by another class so that we get multilevel inheritance
# a derived class inherits from another derived class it creates a chain of inheritance where properties and behaviors of the base class are passed through multiple levels.
# a-> b-> c
class Dadaji:
    def dadaji1(self):
        print("Dada ki Property")
class Betaji(Dadaji):
    def Betaji1(self):
        print("Beta ki Property")
class Potaji(Betaji):
    def Potaji1(self):
        print("Pote ki Property")

property=Potaji() #object of child class potaji
property.dadaji1()# Potaji has access all the methods of dadaji and betaji
property.Betaji1()
property.Potaji1()






class RBI:
    def rbiroi(self):
        accno=12345
        bal=789238
        ir=bal*0.1
        return ir
class SBI(RBI):
    def sbiroi(self):
        return "7%"
class PNB(SBI):
    def pnbroi(self):
        return "6%"
class ICICI(PNB):
    def iciciroi(self):
        return "12%"
ob=ICICI()
print("ICICI ROI is ",ob.iciciroi())
print("SBI ROI is ",ob.sbiroi())
print("RBI ROI is ",ob.rbiroi())









class SBI:
    def sbibank(self,accno):
        self.accno=accno
        lsaccno=[1234,5678,9101,1213,1415]
        lsaccname=["a","b","c","d","e"]
        lsaccbal=[1234,2334,45344,563465,34554]
        for i in lsaccno:
            if(accno==i):
                x=lsaccno.index(accno)
                print("Account Holder Name is : ",lsaccname[x])
                break
            else:
                print("AC No is Not Valid")
ob=SBI()
ob.sbibank(1234)

