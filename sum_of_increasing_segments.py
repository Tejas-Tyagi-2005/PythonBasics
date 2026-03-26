# Find the sum of lengths of all increasing segments

arr = list(map(int,input("Enter the elements of the array :").split()))

sum = 0 # the elements could be 0 

# we will not use any prev_increasing varible , as we do not need count of segments 

for i in range(len(arr)-1):
    if arr[i]> arr[i+1]:
        sum += arr[i]
    else:
        sum = 0 

print(sum)            