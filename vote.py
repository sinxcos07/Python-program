import tkinter as Tk
from tkinter import *
master = Tk()
Label(master, text='xyz').grid(row=0)
Label(master, text='abc').grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
mainloop()
print("                                   welcome        ")
print("candidate 1=xyz")
print("candidate 2=abc")
a=0
b=0
x=int(input("No of votes to be casted="))
for i in range(0,x):
    
    print("vote number",i+1)
    c=input("which candidate u want to vote 1 or 2:")
    
    if c=="1":
         a=a+1
         
    elif c=="2":
         
         b=b+1
         
    else:
           print("candicate number not found in vote number",i+1)
print("vote for candidate 1=",a)
print("vote for candidate 2=",b)
if a>b:
    print("candidate 1 won")
elif b>a:
    print("candidate 2 won")
elif a==b:
    print("its a tie")