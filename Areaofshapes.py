#write programs to find area of all the Shapes  input taken from user
#Area of square
side=int(input("Enter Side of Square : "))
ans=side*side
print(f"Area of Square is : {ans}")

#Area of Rectangle
length=int(input("Enter Length of Rectangle : "))
width=int(input("Enter Width of the Rectangle : "))
ans=length*width
print(f"Area of Rectangle is : {ans}")


#Area of triangle 
base=int(input("Enter Base of the traingle : "))
height=int(input("Enter Height of the traingle :"))
ans= 1/2*base*height
print(f"Area of Traingle is : {ans}")

#Area of Circle
radius=int(input("Enter Radius of the Cirle : "))
ans=3.14*radius*radius
print(f"Area of Circle is : {ans}")
