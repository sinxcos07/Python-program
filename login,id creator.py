import pandas as pd
login_entry={}
a=input("enter email:")
b=input("create password:")
c=input("re-enter the password:")
if b==c:
    print("WELCOME,id was created you can login now")
    login_entry[a]=b
    print(login_entry)

    v=input("enter email:")

    if a in login_entry:
        d=input("enter password:")
        if d in login_entry[a]:
            print("access granted")
            q=float(input("enter the principle amount="))
            w=float(input("enter rate of interest="))
            e=float(input("enter time period="))
            r=(q*w*e)/100
            print("interest amount=",r,"total return=",r+q)
        else:
            print("wrong password")
    else:
        print("email not found")
else:
    print("re-enter the password correctly")
df=pd.DataFrame(login_entry,index=[1])
print(df)




    
    
    