# Find the length of the longest continuous subarray where all elements are equal

arr = list(map(int,input("Enter the elements of the array :").split()))

current_len = 1 # Initial starting bare minimum lenght is assumed to be 1 

max_len = 1

for i in range(len(arr)-1):
    if arr[i] == arr[i+1]:
        current_len += 1
        if current_len > max_len:
            max_len = current_len
    else :
        current_len = 1 

print("The length of the longest continuous subarray where all elements are equal is :",max_len)



