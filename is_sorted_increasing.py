# Check if the array is sorted in increasing order (strictly increasing)
# Print YES or NO


arr = list(map(int,input("Enter the elements of the array :").split()))


# SPEACIAL CASE QUESTION : ASSUME THE ARRAY TO BE SORTED AT FIRST , THEN CORRECT IT 


is_sorted = True 

for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        is_sorted = False
        break 


if is_sorted:  # FOR BOOLEAN VARIABLE U CAN JUST WRITE THE VARIABLE NO NEED TO WRITE " == TRUE/FALSE"
    print("YES")
else :
    print("NO") 

