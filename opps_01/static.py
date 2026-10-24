#Static method don't use the self parameter(work at class level)

class Animal:
    @staticmethod
    def hello():
        print("hello piratesaman")

a1 = Animal()

a1.hello()