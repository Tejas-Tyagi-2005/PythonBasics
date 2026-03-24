# Print all elements in the array that are greater than k

arr = list(map(int,input("Enter the elements : ").split()))

k = int(input("Enter k : "))

for i in arr:
    if i > k:
        print(i)

