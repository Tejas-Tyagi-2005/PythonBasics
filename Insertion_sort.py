

arr = list(map(int,input("Enter the  array :  ").split()))

for i in range(1 , len(arr)): # traverse from first element of unsorted array to the end 
    key = arr[i] # value of key changes in each iteration and stays at the index no i , initially it is index = 1 in the first itertion 
    j = i-1 # the index positon of j is set as 1 before the index of the key 


    while j >= 0 and arr[j] > key: # checks these conditions
        arr[j+1] = arr[j] # sets the value of arr[j+1] to that off [j]
        j = j-1 # send the j pointer back to left one more step to check for any remaining elements to the left . This is a EDGE CASE in the first itertion when there are no elements to the left of j , but we still check 

    arr[j+1] = key # set the value of key to the arr[j+1]      

print("\nbelow is your sorted array  \n") # add \n anywhere to add a blank line 



print(arr)