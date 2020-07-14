def binarySearch(arr, x):
    l = 0
    r = len(arr)-1
    while l <= r:
        mid = l + (r-l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

arr = list(map(int, input().split()))
x = int(input()) 

result = binarySearch(arr, x)
if result != -1:
    print("Element present at", result)
else:
    print("Element not found")