list = []
n = int(input("Enter a count of list : "))
for i in range(n):
    w = int(input("Enter a value : "))
    list.append(w)
x = int(input("Enter a search value : "))
list = sorted(list)
print("search value is ", x, "\n" , "list values is ", list)

def binary_search(number , array , lis , hig):
    if hig < lis:
        return -1
    mid = lis + hig // 2
    if number == array[mid]:
        return mid
    elif number < array[mid]:
        return binary_search(number , array , lis , mid-1)
    else:
        return binary_search(number, array , mid+1 , hig)

def my_search(x , list):
    return binary_search(x , list , 0 , len(list)-1)

pos = my_search(x , list)
if pos < 0:
    print("search value is not found")
else:
    print("search value is :", pos+1)


"""
array = []
count = int(input("Enter a Count Of list : "))
for i in count:
    w = int(input("Enter a value : "))
    array.append(w)
array = sorted(array)
x = int(input("Enter a Search Value : "))
def Binary(val, array , les, hig):
    if les < hig:
        return -1
    mid = les + hig //2
    if array[mid] == val:
        return mid
    elif array[mid] < val:
        return Binary(val, array, les ,mid-1)
    else:
        return Binary(val, array, mid+1, hig)
def start(x, array):
    return Binary(x, array, 0, len(array)-1)
p = start(x, array)
if p < 0:
    print("search value is not found")
else:
    print("search value is :", p +1)


"""
