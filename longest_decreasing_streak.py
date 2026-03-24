# Find the length of the longest continuous decreasing subarray

arr = list(map(int,input("Enter the elements of the array :").split()))

current_lenght = 1 

max_lenght = 1 


for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        current_lenght += 1
        if current_lenght > max_lenght:
            max_lenght = current_lenght
    else :
        current_lenght = 1

print(max_lenght)                