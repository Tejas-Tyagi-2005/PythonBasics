# Write a function that takes a list of numbers  
# and returns the sum of all elements

def sum_list(nums):
    total = 0
    for x in nums:
        total += x
    return total    

nums = [1,2,3,4]


a = sum_list(nums)

print(a)