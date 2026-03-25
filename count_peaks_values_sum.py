# Find the sum of all elements which are greater than both neighbors

arr = list(map(int,input("Enter the elements of the array :").split()))

total = 0 

for i in range(1,len(arr)-1):
    if arr[i]>arr[i+1] and arr[i]>arr[i-1]:
        total += arr[i]


print(total)        