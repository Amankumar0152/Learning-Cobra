# f = open("IO/sample.txt", "a+")

# # f.write("Need for speed")
# f.write("Hello i want to learn Spring Boot")
# f.close()


#with syntax

with open("demo.txt", "r") as f:
    data = f.read()
    print(data)

with open("demo.txt", "w") as f:
    f.write("New Data Insrted")