# Count how many numbers in the array are multiples of 3

arr = list(map(int,input("enter the elements :").split()))

count = 0 

for i in arr:
    if i%3 == 0 :
        count += 1 

print(count) 

