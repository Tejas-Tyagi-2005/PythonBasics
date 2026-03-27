# Write a function that takes a list of numbers  
# and returns the count of positive numbers (> 0)


def positivenum(arr):
    count = 0 
    for i in arr:
        if i > 0 :
            count += 1 
    return count 


print(positivenum([1,2,3,-9,-4,-5,-8]))
    

        

            