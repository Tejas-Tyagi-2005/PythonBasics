# Count how many elements in the array are equal to 0

arr = list(map(int,input("Enter nums to check for zeros  : ").split()))

count = 0 

for i in arr:
    if i ==  0:
        count += 1 
print(count)



