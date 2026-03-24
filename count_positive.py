# Count how many numbers in the array are positive (> 0)

arr = list(map(int,input("Enter nums to count positives : ").split()))


count = 0

for i in arr:
    if i > 0:
        count += 1

print(count)        
