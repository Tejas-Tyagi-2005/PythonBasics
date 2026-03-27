# Write a function that takes a number n  
# and returns the sum of its digits

def sumOfDigits(n):
    total = 0 
    for i in str(n):
        total += int(i) 
    return total 

print(sumOfDigits(999))    

