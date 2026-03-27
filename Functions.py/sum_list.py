# Write a function sum_list(arr)
# Return the sum of all elements in the list using a loop.

def sum_list(arr):
    total = 0 
    for i in arr:
        total += i 
    return total 


print(sum_list([1,2,4]))