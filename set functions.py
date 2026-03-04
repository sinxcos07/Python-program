a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
r = a.union(b)
print("Union:", r)
ir = a.intersection(b)
print("Intersection:", ir)
d = a.difference(b)
print("Difference (A - B):", d)
a.add(6)
print("Set A after adding 6:", a)
b.clear()
print("Set B after clearing:", b)
print("Length of Set A:", len(a))
print("Is 3 in Set A?:", 3 in a)
print("Is 10 in Set A?:", 10 in a)


