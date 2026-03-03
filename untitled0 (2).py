x=[5,3,6,2,1]
ind=[4,3,2,1,0]

for i in x:
    for j in ind:
        if i<=x[j]:
            x[j]=i
            
        

    
print(x) 

