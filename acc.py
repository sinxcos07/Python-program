pas={"qwe":"123","xzc":"324","tyr":"537"}
q=input("already have a account or want to create new account(old/create):")
if q=="old":
   a={}
   b=input("enter the user name:")
   if b in pas.keys():
     print("username found")
     c=(input("enter passcode"))
     if c in pas[b]:
         print("access granted")
         
     else:
         print("wrong password")
   else:
       print("username not found")
elif q=="create" :
    e=input("enter username:")
    g=(input("enter passcode:"))
    pas[e]=g
    print("account created")
    h=input("enter user name:")
    k=input("enter passcode:")
    if h in pas:
        if k in pas[e]:
         print("access granted")
        else:
         print("wrong")
    else:
        print("wrong")
        
else :
    print("cant recognize")
    
    
    
        
        