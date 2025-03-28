s={2,3,4,3}
print(s)
print(type(s))
st={}
print(type(st))   #dictionary 
info={"carla",19,False,5.5,19}
print(info)  #print in unordered way

# accessing set Items using a for loop
for value in info:
    print(value)


s1={1,2,4,6,7}
s2={3,5,6,8}
print(s1.union(s2))  #print s1 and s2 combine in new set
# {1, 2, 3, 4, 5, 6, 7, 8}

s1.update(s2)  #items of s2 will be added to the s1 
print(s1,s2)
# {1, 2, 3, 4, 5, 6, 7, 8} {8, 3, 5, 6}


cities={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities3=cities.intersection(cities2)   #values which are common in both sets
print(cities3)
# {'Madrid', 'Tokyo'}
cities.intersection_update(cities2)   #remove the elements which are not common with element of cities2 
print(cities,cities2)
# {'Madrid', 'Tokyo'} {'Madrid', 'Kabul', 'Seoul', 'Tokyo'}



city={"raipur",'pahawadi',"pawarjhanda","hirawadi"}
city2={"Jampur","Baretha","raipur","pahawadi","shahpur"}
city3=city.difference(city2)
# city3=city.symmetric_difference(city2)
print(city3)
# city.symmetric_difference_update(city2)
# print(city)

# village={"Tokyo","Madrid","Berlin","Delhi"}
# village2={"Tokyo","Seoul","Kabul","Madrid"}
# print(village2.issubset(village))
# village3={"Tokyo","Madrid"}
# print(village3.issubset(village))


village={"Tokyo","Madrid","Berlin","Delhi"}
village2={"Tokyo","Seoul","Kabul","Madrid"}
print(village.issuperset(village2))
village3={"Tokyo","Madrid"}
print(village.issuperset(village3))