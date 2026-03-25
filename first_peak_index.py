# Find the index of the first element that is greater than both neighbors
# If no such element exists, print -1

arr = list(map(int,input("Enter the elements of the array :").split()))

idx = -1 


for i in range(1,(len(arr)-1)):
    if arr[i] > arr[i+1] and arr[i] > arr[i-1]:
        idx = i
        break

print("The index is " ,i)
