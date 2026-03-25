# Find the maximum sum of any continuous strictly increasing subarray

# we need to return the sum of the subarray which is the largest 

arr = list(map(int,input("Enter the elements of the array :").split()))


current_sum  = arr[0] 

max_sum = arr[0]

for i in range(len(arr)-1):
    if arr[i] < arr[i+1]:
        current_sum += arr[i+1]
    else :
        current_sum = arr[i+1] 


    if current_sum > max_sum:
        max_sum = current_sum



print(max_sum)


            