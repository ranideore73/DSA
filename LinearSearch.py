def search(arr, k):
    for i in range(0, len(arr)):
        if (arr[i] == k):
            return i
    return -1
arr = list(map(int, input().split()))
n = len(arr)
k = int(input())
r = search(arr, k)
if (r == -1):
    print("not found")
else:
    print("found at",r)
    