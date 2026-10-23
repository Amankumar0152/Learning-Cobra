# import os

# os.remove("IO/sample.txt")
#Q
# with open("practice.txt", "w") as f:
#     f.write("Hi Everyone\nwe are learning file in IO")
#     f.write("using Java.\nI like Programming in Java")

# with open("practice.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("Java", "Python")
# print(new_data)

# with open("practice.txt", "w") as f:
#     f.write(new_data)

#search text

def check_word():
    word = "xlearning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if(data.find("learning")!= -1):
            print("found")
        else:
            print("not found")

check_word()