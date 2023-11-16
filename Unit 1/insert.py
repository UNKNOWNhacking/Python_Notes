

def insert(list, number):
    i = len(list)
    for a in range(len(list)):
        if list[a] > number:
            i = a
        break
    if i == len(list):
        list = list[:i] + [number]
    else:
        list = list[:i] + [number] + list[i:]
    return list
list = [1, 2, 3, 4, 6,7]
number = 5
print(insert(list, number))
