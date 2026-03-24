# Find the sum of all even numbers in the array


arr = list(map(int,input("Sum of all even numbers  : ").split()))

total = 0 

for i in arr:
    if i%2 == 0:
        total += i 


print(total)