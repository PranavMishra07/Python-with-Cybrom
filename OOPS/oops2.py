class Bank:
    def IRSBI():
        return "7%"
    def ICICI():
        return "7.2%"
    def PNB():
        return "7.5%"
obj=Bank
# obj.PNB()  #don not print the data 
print("IR OF PNB : ",obj.PNB())
print("IR OF IRSBI : ",obj.IRSBI())
print("IR OF ICICI : ",obj.ICICI())
