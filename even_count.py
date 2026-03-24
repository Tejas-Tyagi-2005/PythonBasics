# Count how many numbers in the array are even

arr = list(map(int,input("Enter the elements by space to count the number of evens : ").split()))

count = 0 

for i in arr :
    if i%2 == 0 : # DOUBLE == IS COMPARING , = IS ASSINGMENT
        count += 1


print(count)

