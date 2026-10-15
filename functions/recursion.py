#recursive function
# def show(n):
#     if(n == 0): #base case, there should one conditio9n for stop function
#         return
#     print (n)
#     show(n-1)

# show(10)

#factorial in recursion 

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n

result = fact(4)
print(result)

#Q1

def calcSum(n):
    if(n == 0):
        return 0
    print(n)
    return calcSum(n-1) + n

sum = calcSum(10)
print(sum)

#Q2

 