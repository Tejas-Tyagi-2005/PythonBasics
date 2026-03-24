# Find the sum of all numbers in the array that are divisible by k

arr = list(map(int,input("Enter the elements : ").split()))

K = int(input("The value of K is :"))

total = 0 

for i in arr:
    if i%K == 0:
        total += i 

print(total)        