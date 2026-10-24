#create student class that takes name and marks of 3 subjects as arguments in constructor. Then create a method to print the average.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for value in self.marks:
            sum += value
        print("Hi", self.name, "your avg score is: ", sum/3)
         


s1 = Student("piratesaman", [12, 45,67])

s1.get_avg()

s1.name = "Legolas"

s1.get_avg()