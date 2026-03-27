# Given a number n, return how many digits it has using recursion.
# Example: 1234 → 4

def digit_counter(n):
    if n < 10:
     return 1 
    return 1 + (digit_counter(n//10))
   

print(digit_counter(234463728329))