#creating list by taking one by one value in different variable
x=int(input("enter number:"))
y=int(input("enter number:"))
a=int(input("enter number:"))
g=int(input("enter number:"))
h=int(input("enter number:"))
v=[x,y,a,g,h]
#we can also add elements to list using loops
no_ele=int(input("enter number of element you want in list:"))
l=[]
for x in range(no_ele):
    b=int(input("enter the number :"))
    l.append(b)
print(l)

#program to find if a number is present in list or not
o=int(input("enter number to find:"))
if o in v:
    print("yes number found")
else:
    print("not found")
    
#to find the number at asked index
k=int(input("enter index of number to navigate:"))
print(v[k])

#checking is tuple given are same or different    
q=(1,2,4)
y=(4,5,6)
if q==y:
    print("tuple are same")
else:
    print("tuple are different")