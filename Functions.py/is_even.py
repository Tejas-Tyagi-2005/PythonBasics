# Write a function that takes a number n  
# and returns True if n is even, else False

def even_checker(n):
    if n%2 == 0:
        return True
    else:
        return False
    
x = even_checker(6)
print(x)    