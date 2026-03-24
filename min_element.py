# Find the minimum element in the array

arr = list(map(int,input("Enter elements to find min : ").split()))

min_num = arr[0] # ALWASYS START WITH FIRST ELEMENT WHEN COMPARING


for i in arr:
    if i < min_num :
        min_num = i 

print("The smallest element is : " , min_num)        
