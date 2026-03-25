# Find the length of the longest continuous subarray where elements alternate (up-down or down-up)
# Example: 1 3 2 4 3 → alternating

arr = list(map(int,input("Enter the elements of the array :").split()))

current_len = 1
prev = 0
max_len = 1

for i in range(len(arr)-2):
    if arr[i] < arr[i+1]:
        curr = +1
    elif arr[i] > arr[i+1]:
        curr = -1 
    else :
        curr = 0 


    if curr == 0:
        current_len = 0
    elif curr != prev:
        current_len += 1 
    else :
        current_len = 2 

    prev = curr
    
    if current_len > max_len:
        max_len = current_len

print(max_len)


 