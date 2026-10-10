list = [10, 20, 30]
vag = ["pamidor", "Kartofel", "Ogurets", "banan"]

for nums in list:
    print(nums)


tup = (1, 2, 3, 4, 5, 6) 


str = "piratesaman"

for char in str:
    if(char == 's'):
        print("Found S")
        break
    print(char)
else:
    print("end")

#Q

nums = (1, 2,3,4,5,6,7,8,32,4,564,3,44543,43,54,23)
x= 32
idx = 0
for value in nums:
    if(value == x):
        print("Found")
    idx =+1