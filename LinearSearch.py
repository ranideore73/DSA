def search(arr, n, x):
    for i in range(0,n):
        if (arr[i] == x):
            return i
    return -1

arr = [2,3,4,10,40]
x = 10
n = len(arr)
result = search(arr, n, x)
if (result == -1):
    print("not present")
else:
    print("present at ", result)
    