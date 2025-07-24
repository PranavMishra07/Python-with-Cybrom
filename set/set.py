# s={} empty set is called dictionary() its type is dict
# s={1,2,3,4,5,6,7,8,9}
# print(type(s))  #for check the type of data
# s.add(10)    #to add single data to set
# print(s)
# s.pop()   #randomly delete element from set
# print(s)
# l=[11,12,13]
# s.update(l)
# print(s)
# s.remove(10)
# print(s)
# s.discard(50)  #preffered
# print(s)
# randomly data ko delete pop pop()
# remove se jo element apan pass karenge wahi delete hoga remove(10)
# discard mai enter data hoga to delete hoga nahi to nahi hoga par key error nahi aayega
# add main only one value add add()
# update mai kitni bhi value add kar sakte hai update()  multiple value add




# s1={1,2,3,4,5,6,7,8,9}
# s2={i for i in range (1,5)}
# print(s2)
# print(s1.intersection(s2))   #common element print
# print(s1.union(s2))   #for merging s1 and s2 
# print(s1.difference(s2))  #remove common element from set
# print(s1^s2)  #another way for difference
# print(s2.difference(s1))  #remove common element from set  set(empty)
# x=chr(97)  #for ascci value
# print(x)
# wap to make crud operation on set
s=set()
print(type(s))

# Dictionary
d={
    100:"Ram",
    200:"Shyam",
    300:"Aman"
}
print(d)
x=d.popitem()   #popitem delete random element (key and value) and return key and value - (300, 'Aman')
print(x)
y=d.pop(100)   # pop delete key value and returns deleted value Ram
print(y)
# d.clear()  #clear the dictionary fully empty 
print(d)
d[200]="How are you"   #data update if exist if not exist then add data to dictionary
print(d)    
<<<<<<< HEAD
# in dictionary key are unique if not then the last key will override the key we have before
=======
# in dictionary key are unique if not then the last key will override the key we have before

>>>>>>> 201831275ccafe53f38a9d709c8c6b8a87473f4a
