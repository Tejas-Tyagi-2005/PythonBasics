# Find the length of the first continuous subarray where all elements are equal
# If none exists (no repeats), print 1

arr = list(map(int,input("Enter the elements of the array :").split()))

current_len = 1 

found = False

for i in range(len(arr)-1):
    if arr[i] == arr[i+1]:
        current_len += 1 
        found = True
    else :  
        if found :
            break
        current_len = 1


    
print(current_len)                