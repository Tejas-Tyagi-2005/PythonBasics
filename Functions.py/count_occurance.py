# Write a function count_occurrences(arr, target)
# Return how many times target appears in the list using a loop.


def count_occurance(arr,target):
    count = 0 
    for i in arr:
        if i == target:
            count += 1
    return count 


print(count_occurance([1,4,3,4,4,6,7,8,9,],4))