# Check if the array is sorted in decreasing order (strictly decreasing)
# Print YES or NO


arr = list(map(int,input("Enter the elements of the array :").split()))


is_sorted = True # ASSUMING THE ARRAY TO BE DECREASING TOWARDS THE RIGHT 

for i in range(len(arr)-1):
    if arr[i]<arr[i+1]: #CHECKING IF THE ELEMENTS IS DECREASING TO THE RIGHT OR NOT 
        is_sorted = False 
        break 

if is_sorted:
    print("YES")
else :
    print("NO")        