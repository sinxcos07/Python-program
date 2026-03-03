text="afsgsdfjhg"
count={}
l=[]
for index in text:
    if index not in l:
        l.append(index)
        count[index]=0
    count[index]=count[index]+1
print(count)