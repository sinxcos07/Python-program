import cmath
a=int(input("enter a:"))

b=int(input("enter b:"))

c=int(input("enter c:"))

d=(b**2)-(4*a*c)
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)
print ("root:",sol1)

print ("root:",sol2)

