# i = 1
# while i <=100:
#     print(i)
#     i += 1

# print("This loop ended")

# i = 100
# while i >=1:
#     print(i)
#     i -= 1

# num = int(input("Enter a Numner to print table: "))

# i = 1
# while i <= 10:
#     print(num *i)
#     i +=1 

#4
# nums = [1, 2, 3,34, 56, 67, 68, 78, 89, 90]
# heroes = ["Ironman", "antman","pirates"]
# idx = 0
# while idx < len(nums):
#     print(heroes[idx])
#     idx +=1

#5
nums = (1, 4, 9,16, 25, 36, 49, 64, 81, 100)
x = 36

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("Found at idx", i)
        break
    i += 1