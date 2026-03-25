# Find the length of the longest continuous subarray where all elements are equal

arr = list(map(int,input("Enter the elements of the array :").split()))

current_len = 1 # becasue the smallest lenght of the subarry is 1 

max_len = 1

for i in range(len(arr)-1):
    if arr[i] == arr[i+1]: # if elements are equal
        current_len += 1 # add to the lenght of the sub array 
    else :
        current_len = 1

    if current_len > max_len:
        max_len = current_len

print(max_len)                 