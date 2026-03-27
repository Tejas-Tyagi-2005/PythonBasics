# Write a function find_max(arr)
# Return the maximum element in the list using a loop.

def find_max(arr):
    max = arr[0] 
    for i in range(len(arr)):
        if max < arr[i]:
            max = arr[i]
    return max 


print(find_max([1,2,3,4,5,8,7,6,9]))
