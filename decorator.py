def decor(func):
    def inner(name):
        if name=="Vedant":
            print("hello",name,"how are you")
        else:
            func(name)
    return inner
@decor

def myfunc(name):
    print(name,"chale ja bhai")

# myfunc("Vedant Chandekar")Vedant Chandekar chale ja bhai
myfunc("Vedant")