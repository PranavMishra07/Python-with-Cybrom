l1=[1,2,3,4,5,6,"Harry",True]
# print(type(l1))
# print(l1)
# print(l1[0])
# print(l1[1])
# print(l1[2])
# print(l1[3])
# print(l1[4])
# print(l1[-3]) #Negative indexes
# print(l1[len(l1)-3]) #Positive Indexes

# we can check if a given item is present in the list or not using in keyword
# if 3 in l1:
#     print("YEs")
# else:
#     print("NO")

# if "Har" in l1[-2]:  #for "Harry" string
#     print("Yes")
# else:
#     print("No")


if "Harr" in  "Harry":  #for "Harry" string
    print("Yes")
else:
    print("No")

print(l1[:])  # for printing full list
print(l1[4:])  # using positive indexes  from 4rth index to till the end


# Negative indexing access item from the end of the list the last item has index[-1]
print(l1[-4:])  #using Negative Indexes 

print(l1[-4:-1])
print(l1[-6:-1:2])  # print alternative index by 2
# [1, 2, 3, 12, 123]


# sort()-- this method sort the list in ascending order the original list is updated
l=[12,123,1,2,3]
l.sort()
print(l)
# [1, 2, 3, 12, 123]


color=["voilet","indigo","blue","green"]  #ascending order by  alphabetical order
color.sort()
print(color)
# ['blue', 'green', 'indigo', 'voilet']


# if we want to print list in decending order we must give reverse=True as a parameter in the sort method  this is the parameter of sort method

l.sort(reverse=True)
print(l)
# [123, 12, 3, 2, 1]

color.sort(reverse=True)
print(color)
# ['voilet', 'indigo', 'green', 'blue']


# reverse() method reverse the order of the list
res=[1,2,3,20,45,64]
res.reverse()
print(res)
# [64, 45, 20, 3, 2, 1]

# index() Method returns the index of the first occurence of the list item
index=[11,2,12,1,4,5,6]
print(index.index(1))
# 3

std=["Pranav","Himanshu","Sajal","Tinu"]
print(std.index("Sajal"))
# 2


# Count() method returns the count of the number of items with the given value
cnt=[1,2,3,4,5,1,1,23,1,9]
print(cnt.count(1))
# 4


# Copy() - returns copy of the list this can be done  to perform operation on the list without modifying the original list
# in this way original list is modyfied without copy method
cp=[1,2,3,4,5,6,7,8,9]
m=cp
m[0]=10
print(m)
print(cp)
# with copy() method
cpy=[1,2,4,5,6,7,8,9]
n=cpy.copy()
n[0]=20
print(n)
# [20, 2, 4, 5, 6, 7, 8, 9]
print(cpy)
# [1, 2, 4, 5, 6, 7, 8, 9]

# append() - this method appends itens to the end of the existing list
app=[1,2,3,4,5,6]
app.append(99)
print(app)
# [1, 2, 3, 4, 5, 6, 99]

# insert() - this method insert an item at the given index user has to specify the index and the item to be inserted within the insert() method
ins=[1,2,3,4,5,6]
ins.insert(1,999)
print(ins)
# [1, 999, 2, 3, 4, 5, 6]

# extend() - this method adds entire list or any other collections datatype(set,tuple.dictionary) to the existing list

ex=[1,2,3,4,5,6]
ls=[10,20,30,40]
ex.extend(ls)
print(ex)
# [1, 2, 3, 4, 5, 6, 10, 20, 30, 40]


po=[1,2,34,4,5]
po.pop(1)
poped=po.pop(2)
print(po)
print(poped)
# [1, 34, 4, 5]


re=[1,2,1,4,5,6]
re.remove(2)
print(re)
# re.clear()

print(re)


cnt=[1,2,3,4,4,5,6,4]
print(cnt)
print(cnt.count(4))
