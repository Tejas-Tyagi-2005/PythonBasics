# Count how many continuous strictly increasing segments exist in the array

arr = list(map(int,input("Enter the elements of the array :").split()))


count = 0 

prev_increasing = False

for i in range(len(arr)-1):
    if arr[i]<arr[i+1]:
        if prev_increasing:
            count += 1
        prev_increasing = True     
    else :
        prev_increasing = False  

print(count)


       