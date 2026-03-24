# Count how many numbers in the array are greater than 5


arr = list(map(int,input("Enter the elements of the array : ").split())) # taking the arr as input


count = 0 

for i in range(len(arr)): # looping over the array 
    if arr[i] > 5 :
        count = count + 1 

print(count)