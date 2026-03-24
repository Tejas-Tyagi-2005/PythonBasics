# Count how many elements in the array are less than k

arr = list(map(int,input("Enter the elements :").split()))


k = int(input("Enter the value of k :"))

count = 0 

for i in arr:
    if i < k:
        count += 1 

print(count)

