def calculate(a, n):
    for i in range(1 , n+1):
        b = a[i:] + a[:i]
        print("circulation", i, "= ", b)
    return
a = [91,92,93,94,95]
n = int(input("Enter a N : "))
calculate(a, n)

