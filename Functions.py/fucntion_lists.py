# Write a function that takes a list of numbers  
# and returns a new list where each element is squared  
# (use another function inside)


def square(x):
    return x*x

def squareList(arr):
    result = []
    for i in arr:
        result.append(square(i))
    return result 
    

print(squareList([1,2,3]))
  