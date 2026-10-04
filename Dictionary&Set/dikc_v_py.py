#Dictionary in python

data = {'aman':92, 'rahul':85, 'sachin':78, 'rohit':88}

print(data.get('sh', 'not found'))  # Output: 92

data.pop('sachin')  # Removes the key 'sachin' from the dictionary
data['sh'] = 95  # Adds a new key-value pair to the dictionary
print(data)