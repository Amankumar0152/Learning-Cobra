list1 = [1,2,1]
list2 = [1,2,3]

copylist1 = list1.copy()
copylist1.reverse()

if(copylist1 == list1):
    print("pelindrome")
else:
    print("not pelindrome")