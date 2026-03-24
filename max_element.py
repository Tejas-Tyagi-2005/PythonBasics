# Find the maximum element in the array

arr = list(map(int,input("enter element to find max in a arr :").split()))


max_num = arr[0]

for i in range(len(arr)):
    if arr[i] > max_num :
        max_num = arr[i]

print(max_num)




