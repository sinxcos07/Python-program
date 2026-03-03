a = "Hello"
b = "World"
concatenated_string = a + " " + b
print("Concatenated String:", concatenated_string)
repeated_string = a * 3
print("Repeated String:", repeated_string)
print(a[0]) 
print(a[-1])  
print(a[1:4]) 
print("length of string=", len(a))
upper_case = a.upper()
lower_case = b.lower()
print("Uppercase:", upper_case)
print("Lowercase:", lower_case)
il = a.find("l") 
print("Index of 'l' in 'Hello':", il)
l = a.count("l")
print("Count of 'l' in 'Hello':", l)
print("Characters in 'Hello':")
for i in a:
    print(i)
