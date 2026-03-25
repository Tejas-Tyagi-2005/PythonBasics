# Count how many strictly decreasing subarrays exist in the array


arr = list(map(int,input("Enter the elements of the array :").split()))

current = 1

count = 1

for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        current += 1
    else:
        current = 1 

    count += current 

print(count)
            