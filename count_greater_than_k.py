# Count how many numbers in the array are greater than a given number k


arr = list(map(int,input("Enter elements : ").split()))

k = int(input("Enter the number k : ")) # the number to compare with 

count = 0 

for i in arr:
    if i > k:
        count += 1 

print(count)


