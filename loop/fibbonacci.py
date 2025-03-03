# wap to print fibbonacci series input taken from user
n=int(input("Enter any Number : "))
i=0
t1=0
t2=1
# print(f"Fibonacci Series : {t1} ,{t2}")
while(i<n):
    print( t1, )
    t3=t1+t2
    t1=t2
    t2=t3
    i+=1

n=int(input("Enter any Number : "))
i=0
t1=0
t2=1
t3=0
print(f"Fibonacci Series : {t1} ,{t2}")
while(i<n):
    print(f"{t1}")
    fibo=t1+t2
    t1=t2
    t2=fibo
    i+=1