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
print(dic["surya"])
print(len(dic))
print(len(cds))#len count no of key
d2=dic.copy()
print(d2)
d2.clear()
print(d2)
print(str(dic))
print(dic.get("avi"))#give value of key
print(dic.items())#give dictionary in tuple form 
print(dic.keys())
dic.update(cds)
print(dic)
print(dic.values())
#print(dic.iteritems()) is removed also has_key is removed
