class Animal:
    college_name = "abc"
    name = "Aman"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
            print("Welcome student", self.name)

    def getmarks(self):
            return self.marks
        
s1 = Animal("piratesaman", 98)
s1.welcome()
print(s1.getmarks)