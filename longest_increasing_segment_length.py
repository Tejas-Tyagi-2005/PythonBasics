# Find the length of the longest continuous strictly increasing segment

arr = list(map(int,input("Enter the elements of the array :").split()))

curren_len = 1 # the logic to keep this 0 is because it is possible that there none increasing segments 

max_len = 1 



for i in range(len(arr)-1):
    if arr[i] < arr[i+1]:
            curren_len += 1 

    else :
         curren_len = 1        

    if curren_len > max_len:
        max_len = curren_len

print(max_len)                    


