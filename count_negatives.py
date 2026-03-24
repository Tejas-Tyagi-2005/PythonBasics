# Count how many numbers in the array are negative (< 0)


arr = list(map(int,input(" check number of negative elements : ").split()))


count = 0 

for i in arr:
    if i < 0 :
        count += 1

print(count)

