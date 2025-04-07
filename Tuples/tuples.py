# tuples whenever we want to represent a grpup of individual object into an single entity where duplicate and homogenius and iterigenius object is to be allow and insertion order is to be preserved but we want immutable behavior of the object then we will use a tuple

# every tuple representing all the object element within () with,seperator
# tuple function
tupl1=(1,2,3,4,5)
print(tupl1)
print(type(tupl1))
x=max(tupl1)
print(x)

#change tuple to list
ls=list(tupl1)
ls.append("Append")
tupl2=["extend","green","yellow"]
ls.extend(tupl2)

# change list to tuple
tupl1=tuple(ls)
print(tupl1)


# write a program to make a crud operation on tuple
# wap to take two input from user and append all the prime number in a list

# methods / function of a tuple

# 1: length()
# 2: max()
# 3: min()
# 4: count()
# 5: list()
# 6: index()

# set 
# Whenever we want to represent group of individual object as an single entity where duplicate object is not to be allowed and insertion order is not preserved then we can use a set
# every set representing all the object element within {} with,seperator
# duplicate ko discard karta hai
# data type alag alag ho sakta hai
# set is mutable

set1={1,2,4,5,6,6,7}
print(set1)
print(max(set1))
print(min(set1))
print(sum(set1))
set1.add("hello added to set")
<<<<<<< HEAD
print(set1)
=======
print(set1)

>>>>>>> 201831275ccafe53f38a9d709c8c6b8a87473f4a
