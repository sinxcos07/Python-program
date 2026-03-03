import openpyxl
wb=openpyxl.Workbook()

w=input("do you want to create id:")

    
if w=="yes":
         a=input("enter a new username:")
         b=int(input("enter passcode:"))
         ws=wb.active
         
         data=(
                 "username","passcode"),(a,b)
         for i in data:
                ws.append(i)
                wb.save("passcode.xlsx")

else:
         print("okk")
