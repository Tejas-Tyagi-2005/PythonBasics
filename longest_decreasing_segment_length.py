# Find the length of the longest continuous strictly decreasing segment

arr = list(map(int,input("Enter the elements of the array :").split()))


Current_len = 1 

max_len = 1 


for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        Current_len += 1
    else :
        Current_len = 1

    if max_len < Current_len:
        max_len = Current_len



print(max_len)