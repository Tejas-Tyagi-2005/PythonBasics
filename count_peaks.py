# Count how many elements are greater than both neighbors (arr[i] > arr[i-1] and arr[i] > arr[i+1])


arr = list(map(int,input("Enter the elements of the array :").split()))


count = 0 

for i in range(1,(len(arr)-1)):
    if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
        count += 1

print(count)

