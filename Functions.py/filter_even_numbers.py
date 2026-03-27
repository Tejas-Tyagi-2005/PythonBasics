# Write a function that takes a list of numbers  
# and returns a new list containing only the even numbers  
# (use another function inside)

def even_filter(arr):
    even_arr = []
    for i in arr:
        if i%2 == 0:
            even_arr.append(i)
    return even_arr        


print(even_filter([1,2,3,4,5,6,7,8,76,5,4,3,7,89,76,54,3,5,6654,3]))            