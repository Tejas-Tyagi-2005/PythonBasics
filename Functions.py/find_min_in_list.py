# Write a function that takes a list of numbers  
# and returns the smallest element

def smallest_num(arr):
    smallest_element = arr[0] 

    for i in range(len(arr)):
        if smallest_element > arr[i] :
            smallest_element = arr[i] 

    return smallest_element

print(smallest_num([1,2,3,4,5,6,-8]))

