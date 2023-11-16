list = [1,2,3,4,5,6,7,8,9,0]
print("Value in list ",list)
number = int(input("Enter a searching value : "))
i = value = 0
while i < len(list):
    if list[i] == number :
        value = 1
        break
    i += 1
if value == 1 :
    print("search value is ", i + 1)
else:
    print("value not found")

"""
l = [1, 2, 3 4, 5]
print("list value is ", l)
i = value = 0
while i < len(l):
    if l[i] == num :
        value = 1
        break
    i += 1
if value == 1:
    print("search value is ", i+1)
else:
    print("value not found")
"""
