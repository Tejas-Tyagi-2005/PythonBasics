# Write a function count_even(arr)
# Return how many even numbers are in the list.

def count_even(arr):
    count = 0 
    for i in arr:
        if i%2 == 0 :
            count += 1 
    return count 

print(count_even([1,2,3,4,5,6]))
