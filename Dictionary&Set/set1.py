collection = {1, 2,2, 3, 3, 4, "Hello", "world", "world"}

print(collection)
print(type(collection))
print(len(collection))

collection1 = set() # way to create empty set
collection1.add(1)
collection1.add(2)
print(type(collection1))
print(collection1)
#collection1.clear()
print(len(collection1))

collection2 = {"Hello", "Pirates", "Welcome", "Caribbean"}

print(collection2.pop()) #pop method can remove anyone random string from set
print(collection2.pop())