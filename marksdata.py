import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
x=int(input("enter number of subjects to calculate the average"))
d=0
for i in range(0,x):
    y=float(input("enter the marks :"))
    d+=y
    
avg=d/x
print("average is :",avg)
t=input("do you want to see the chart according to your marks in subject:")
if t=="yes":
    print("sure")
    s=int(input("enter the total number of marks:"))
    l=[]
    for i in range(0,s,-1):
        l.append(i)
    g=np.arange(0,s)
    o=[]
    for j in range(0,s):
        v=float(input("enter marks  :"))
        o.append(v)        
    plt.bar(g,o)
    plt.show()
else:
    print("okk")
c=pd.DataFrame(o,g,columns=["marks"])
print(c)