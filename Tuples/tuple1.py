countries=("China","india","America","Japan")
print(countries)
print(type(countries))
list1=list(countries)
print(list1)
list1.pop()
print(list1)
list1.append("ShriLanka")
print(list1)
list1[0]="Chad"
print(list1)
countries=tuple(list1)
print(countries)

# we can concatinate two tuples to a new tuple
cont1=("China","india","America","Japan")
cont2=("Chad","shrilanka","Indonesia","Burma")
cont3=cont1+cont2
print(cont3)