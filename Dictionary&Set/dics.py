info = {
    "key" : "value",
    "name" : "Aman",
    "Age" : 23,
    "is_Adult" : True,
    "subjects" : ["Python", "Java", "Spring", "Autumn"],
    "marks" : 53.23
}
print(info)
print(info["subjects"])

# Methods in Dictionary 
print(info.keys()) #return all keys
print(info.values()) #return all values of keys
print(info.items()) # return all key and values in pairs
print(info.get("name"))
print(info.get("subjects"))
new_dict = {"City" : "Varanasi"}
info.update(new_dict)
print(info)