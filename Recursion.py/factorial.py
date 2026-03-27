# Write a function factorial(n)
# Return n! using recursion.

def factorial(n):
    if n == 1: 
     return 1 
    
    return n*(factorial(n-1))

print(factorial(5))