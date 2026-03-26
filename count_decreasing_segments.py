# Count how many continuous strictly decreasing segments exist in the array

arr = list(map(int,input("Enter the elements of the array :").split()))

count = 0 

prev_decreasing = False 

for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        if prev_decreasing == False :
            count += 1 
        prev_decreasing = True
    else:
        prev_decreasing = False 


print(count)        

