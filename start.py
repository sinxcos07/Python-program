import csv
with open("password.csv","w",newline='') as file:
    myfile=csv.writer(file)
    myfile.writerow(["username","password"])
    sno=int(input("no of id u want:"))
    for i in range (sno):
        a=input("username:"+str(i+1))
        b=int(input("passcode:"+str(i+1)))
        myfile.writerow([a,b])