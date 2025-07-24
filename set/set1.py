# Sets are unordered collection of data items they store multiple items in a single variable set items are seperates by commas and enclosed within the curly brackets{}
# s={2,3,4,3}
# print(s)
# print(type(s))
# st={}
# print(type(st))   #dictionary 
# info={"carla",19,False,5.5,19}
# print(info)  #print in unordered way

# accessing set Items using a for loop or iterating
# for value in info:
#     print(value)

# #thw union method print all items that are present in the two sets in the new set but s1 and s2 are untouched
# s1={1,2,4,6,7}
# s2={3,5,6,8}
# s3=s1.union(s2)
# print(s3)
# {1, 2, 3, 4, 5, 6, 7, 8}
# print(s1.union(s2))  #print s1 and s2 combine in new set
# # {1, 2, 3, 4, 5, 6, 7, 8}

## update() method adds items to the existing set from another set
# s1.update(s2)  #items of s2 will be added to the s1 
# print(s1,s2)
# {1, 2, 3, 4, 5, 6, 7, 8} {8, 3, 5, 6}

## intersection() method print only items that are similar in both the sets
# cities={"Tokyo","Madrid","Berlin","Delhi"}
# cities2={"Tokyo","Seoul","Kabul","Madrid"}
# cities3=cities.intersection(cities2)   #values which are common in both sets
# print(cities3)    #Madrid and tokyo are common in both the sets
# # {'Madrid', 'Tokyo'}
# cities.intersection_update(cities2)   #update the existing set cities from another set
# print(cities,cities2)
# # {'Madrid', 'Tokyo'} {'Madrid', 'Kabul', 'Seoul', 'Tokyo'}


# # symmentric_difference print only items that are not similar in both the sets
# city={"raipur",'pahawadi',"pawarjhanda","hirawadi"}
# city2={"Jampur","Baretha","raipur","pahawadi","shahpur"}
# city3=city.difference(city2)  # returns a new set with elements in the first set but not in the second set
# city3=city.symmetric_difference(city2)
# print(city3)
# city.symmetric_difference_update(city2)
# print(city)

##isdisjoint() returns true if sets have no element common 
##issubset() returns true if all elements of the first set exist in the second set
# village={"Tokyo","Madrid","Berlin","Delhi"}
# village2={"Tokyo","Seoul","Kabul","Madrid"}
# print(village2.issubset(village)) #false
# print(village.isdisjoint(village2)) #false
# village3={"Tokyo","Madrid"}
# print(village3.issubset(village)) #true

##issuperset() method return true if the first set contains all the elements of the second set
# village={"Tokyo","Madrid","Berlin","Delhi"}
# village2={"Tokyo","Seoul","Kabul","Madrid"}
# print(village.issuperset(village2))  #false
# village3={"Tokyo","Madrid"}
# print(village.issuperset(village3)) #true


st={12,13,435,45,"GHello"}
print(st)
st.add("gi")  # add only one element at a time print(st)

# st.remove(12) #remove one item at a time  raises an error if not found
# print(st)

# st.discard(10) #remove specific one item at a time not raise a error if parameter is not found
# print(st.pop() )#remove randomly delete an element from the set and return it
st.clear()
<<<<<<< HEAD
print(st)  #Remove all the element from the set
=======
print(st)  #Remove all the element from the set
>>>>>>> 201831275ccafe53f38a9d709c8c6b8a87473f4a
