# Find the sum of all numbers in the array that are multiples of 3

arr = list(map(int,input("Enter the elements :").split()))

total = 0 

for i in arr:
    if i%3 == 0 :
        total += i 

print(total)

