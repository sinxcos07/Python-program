a="pass@123"
b=input("ENTER THE PASSWORD:")
if a==b:
    print("access granted ")
    d=input("which program you want to enter [menu or order]: ")
    if d=="menu":
        print("MOMOS")
        print("PIZZA (medium)")
        print("BURGER")
        print("FRENCH FRIES")
        print("TEA OR COFFEE")
    elif d=="order":
        o=input("Enter your order:")
        if o=="momos":
            k=input("full or half")
            if k=="full":
                print("bill 50rs")
            elif k=="half":
                print("bill 25rs")
        elif o=="pizza":
            print("bill 250rs")
        elif o=="burger":
            print("bill 60rs")
        elif o=="french fries":
            print("bill 50 rs")
        elif o=="tea" or o=="coffee":
            print ("bill 20rs")
    else:
        print("sorry this program is not available")
else:
    print("access denied")