login_entry={}
a=input("enter email:")
b=input("create password:")
c=input("re-enter the password:")
if b==c:
    login_entry[a]=c
    print(login_entry)
else:
    print("Please enter same password")
x=str(login_entry)
f=open("pass.txt","a")
f.write(x)
f.close()
