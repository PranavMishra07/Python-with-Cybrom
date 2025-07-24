# mysql - python can be used in databased applications . one of the most popular database is Mysql
# Mysql is RDBMS (Relational database Management) Software in Which we can create database and One database can have multiple Tables
# PIP - (Python Installer Packages) - to install Liabraries of python in our system or drivers we can use pip

# Commands:-1:  pip install mysql     message show -Successfully installed mysql-0.0.3 mysqlclient-2.2.7
# Commands:-2:  pip install mysql-connector-python   message show - Successfully installed mysql-connector-python-9.2.0


# After installing sucessfull-: write this code to the .py file to check instalation is successful or not

                            #  import mysql.connector
                            # print("connction succesfully")
import mysql.connector
print("connction succesfully")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="crudpython"
)
mycursor=mydb.cursor()
print("Record Management System")
ch=int(input("Enter Your Choice"))
if ch==1:
    rollno=input("Enter Your roll No : ")
    name=input("Enter Your Name : ")
    address=input("Enter Address : ")
    class1=input("Enter Class : ")
    sql="Insert into data (rollno,name,address,class) values(%s,%s,%s,%s)"
    value=[rollno,name,address,class1]
    mycursor.execute(sql,value)
    mydb.commit()
    print("added Successfully")

# import mysql.connector

# import mysql.connector

