import bisect
def insert(list, n):
    bisect.insort(list, n) 
    return list
list = [1, 2, 4]
n = 3
print(insert(list, n))
