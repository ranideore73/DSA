import math 
  
def jumpSearch( arr , x): 

    n = len(arr)  
    step = math.sqrt(n) 
      
    prev = 0
    while arr[int(min(step, n)-1)] < x: 
        prev = step 
        step += math.sqrt(n) 
        if prev >= n: 
            return -1
      
    
    while arr[int(prev)] < x: 
        prev += 1
          
        
        if prev == min(step, n): 
            return -1
      
    
    if arr[int(prev)] == x: 
        return prev 
      
    return -1
  

arr = list(map(int, input("Enter array:").split()))
x = int(input())
 
   
index = jumpSearch(arr, x) 
  
# Print the index where 'x' is located 
print("Number" , x, "is at index" ,"%.0f"%index) 