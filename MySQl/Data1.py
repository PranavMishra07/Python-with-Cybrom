import mysql.connector
print("Connection Successfull")
mydb =  mysql.connector.connect(
           host="localhost",
           user="root",
           password="",
           database="datatable"
)
print("Connection success")
mycursor=mydb.cursor()
print("RECORD MANAGEMENT SYSTEM")
ch=int(input("Enter The Choice : "))
if(ch==1):
       Rollno=int(input("Enter Your Roll no : "))
       Name=input("Enter Your Name : ")
       Address=input("Enter Address : ")
       class1=input("Enter Class : ")
       sql="Insert into datatable (Rollno,Name,Address,Class) values(%s,%s,%s,%s)"
       value=[Rollno,Name,Address,class1]
       mycursor.execute(sql,value)
       mydb.commit()
       print("Data Added Successfully")
