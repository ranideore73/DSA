def interpolationSearch(arr, x):
    n = len(arr)
    lo = 0
    hi = (n - 1) 
   
    while lo <= hi and x >= arr[lo] and x <= arr[hi]: 
        if lo == hi: 
            if arr[lo] == x:  
                return lo
            return -1 
          
         
        pos  = lo + int(((float(hi - lo) / 
            ( arr[hi] - arr[lo])) * ( x - arr[lo]))) 
  
       
        if arr[pos] == x: 
            return pos 
   
        
        if arr[pos] < x: 
            lo = pos + 1
   
        
        else: 
            hi = pos - 1
      
    return -1
  
 
arr = list(map(int,input("Insert sorted array only:").split()))
x = int(input("Enter the element to find:"))
  
r = interpolationSearch(arr, x)

if r == -1:
    print("Element not present")
else:
    print("Element present at", r)
