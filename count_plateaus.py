# Count how many times two consecutive elements are equal

arr = list(map(int,input("Enter the elements of the array :").split()))

count = 0 

for i in range(len(arr)-1):
    if arr[i] == arr[i+1]:
        count += 1 

print(count)
        