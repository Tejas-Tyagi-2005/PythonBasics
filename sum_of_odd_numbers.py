# Find the sum of all odd numbers in the array


arr = list(map(int,input("Enter odd nums to be added  : ").split()))

total = 0 

for i in arr:
    if i%2 == 0:
        total += 0 
    else: total += i

print(total)      