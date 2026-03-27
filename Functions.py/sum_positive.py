# Write a function sum_positive(arr)
# Return the sum of all positive numbers in the list.

def sum_positive(arr):
    total = 0
    for i in arr:
        if i > 0 :
            total += i 
    return total 


print(sum_positive([-3,-4,-9,9]))