print("                                 welcome")
print("candidate 1 name = abc")
print("candidate 2 name = xyz")
v=int(input("enter the number of votes to be casted="))
a=0
b=0
for i in range(0,v):
    c=input("which camdidate you want to vote 1 or 2:")
    if c=="1":
        a=a+1
    elif c=="2":
        b=b+1
    else:
        print("candidate not found in vote number",i+1)
print("vote for candidate 1=",a)
print("vote for candidate 2=",b)
if a>b:
    print("candidate 1 has won")
elif b>a:
    print("candidate 2 has won")
else :
    print("its a tie")
    