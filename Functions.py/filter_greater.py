# Write a function filter_greater(arr, x)
# Return a new list of elements greater than x.

def filter_greater(arr,x):
    greater = []
    for i in arr:
        if i > x:
            greater.append(i)
        
    return greater 


print(filter_greater([1,2,3,4,5,],3))
