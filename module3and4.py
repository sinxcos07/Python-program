x=int(input("enter number:"))
y=int(input("enter number:"))
print(x+y,x*y,x**y,x/y,x%y)
if x>y:
    print("x is greater")
else:
    print("y is greater")
    
d=x>y
print("is x greater?",d)
z=int(input("enter number:"))
if z>y or x>y:
    if x>z:
        print("x is largest")
    else:
        print("z is largest")
else:
    print("y is largest")

lst=[x,y,z]
d=int(input("enter number to check if present in list:"))
if d in lst:
    print("yes {} is present".format(d))
else:
    print("not found")
    
print("Variable swapping")
x,y=50,60
y,x=x,y
