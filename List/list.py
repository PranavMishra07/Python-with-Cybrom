l1=[1,2,3,4,5,"Harry",True]
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


if "Har" in  "Harry":  #for "Harry" string
    print("Yes")
else:
    print("No")

print(l1[:])  # for printing full list
print(l1[4:])  # using positive indexes  from 4rth index to till the end


# Negative indexing access item from the end of the list the last item has index[-1]
print(l1[-4:])  #using Negative Indexes 

print(l1[-4:-1])
print(l1[-6:-1:2])  # print alternative index by 2