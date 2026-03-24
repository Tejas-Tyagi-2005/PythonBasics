# Find the second largest element in the array (without sorting)


arr = list(map(int,input("Enter the array :").split()))


largest = float("-inf") # used to assing smallest value to the variable 

second_largest = float("-inf")

for i in arr:
    if i > largest:
        second_largest = largest
        largest = i 
    elif  i < largest and i > second_largest:
        second_largest = i 

print("The largest is :",largest)

print("The second largest is : ",second_largest)


        



