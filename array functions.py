import array
import numpy as np
a=array.array("i",[1,2,3])
b=np.array([1,2,3,4,5,6])
c=np.array([[1,2],[3,4]])#2d
f=np.arange(1,20)#or use linespace
a[2]=10
len(a)
a.append(7)
a.insert(2,9)#2 is index
a.extend([6,5,4])
print(a.pop(2))#print removed number
print(b[::-1])
print(b[::2])
print(a)
c=[4,5,6]
c.reverse()
print(c)
x=list(reversed(a))
new=np.flip(b)
a.remove(7)
print(a)
d=a[1:4]
print(d)
new=np.array([1,2,3,4])
new2=np.array([4,5,6,7])
l=new==new2
print(l)
t=new.view()#refer to same memory location where as .copy creates independent copy of data
print(t)
print(id(t))
#for alias arraynew=arrayold
great=new>new2
print(great)
less=new<new2
print(less)
g=np.any(less)#tells if any elements follow condition
y=np.all(less)#tell if all elements follow condition
print(g)
print(y)
checkand=np.logical_and(new>10,new2<2)
print(checkand)
ch=np.logical_or(new<10,new2<100)
print(ch)
for i in new:
    print(i)
    
print(new[2])


#todays work 3d matrix
mat=np.array([[1,2,3],[4,5,6]])
mat2=np.array([[9,8,7],[6,5,4]])
print(mat)
print("mat")
print(mat.shape)
print("mat shape")
mat3=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(mat3)
print("mat 3d")
mat=mat.reshape(3,2)
print(mat)
print("mat reshaped")
zers=np.zeros((3,3),int)
print(zers)
print("zeros matrix")
on=np.ones((1,2),int)
print(on)
print("ones matrix")
j=mat+2
print(j)
print("two added in mat")
eee=np.array([[5,6,7],[3,4,5]])
ee=mat2+eee
print(ee)
print("addition of 2 matrix")
dic={"surya":1,"avi":2}
cds={"class1":{"ss":1,"se":2},"class2":{"ty":4,"gh":45}}
print(cds)
dic["way"]=3
print(dic)
dic["avi"]=5
del dic["way"]
dic["wy"]=3
h=dic.pop("wy")
print(dic)

for i in cds:
    print(i)
for i in cds.values():
    print(i)
dic["lst"]=[1,2,3,4,5]
print(dic)