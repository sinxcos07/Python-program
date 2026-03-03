id={"xyz":"123","abc":"332"}
a=input("enter name:")
b=input("enter password:")
if a in id:
   if b in id[a]:
       print("welcome",a)
       c=float(input("enter number 1:"))
       d=float(input("enter number 2:"))
       e=c+d
       print("result",e)
   else:
        print("incorrect password")
else:
    print("user not found")