x=int(input("total no of element to enter:"))
y={}
for i in range(0,x):
    g=float(input("enter element number:"))
    y[i]=g

xi=0
for a in y.values():
    xi+=a
mean=xi/x #correct
print("mean =",mean)

t=0 #t is abs value
n=0 #n is square of abs error
f=0 #f stores sum of square of abs error
for w in y.values():
    t=abs(w-mean)
    n=t*t
    f+=n

var=f/x #variance
print("variance =",var)
sd=var**(1/2)
print("standard deviation=",sd)  