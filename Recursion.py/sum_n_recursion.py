# Write a function sum_n(n)
# Return sum of numbers from 1 to n using recursion.

def sum_n(n):
    if n == 1: 
     return 1
    
    return n + (sum_n(n-1))
 

print(sum_n(3)) 