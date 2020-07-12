def search(arr, n, k):
    for i in range(0, n):
        if (arr[i] == k):
            return i
    return -1
arr = list(map(int, input().split()))
n = len(arr)
k = int(input())
r = search(arr, n, k)
if (r == -1):
    print("not found")
else:
    print("found at",r)
    