# Count how many elements in the array are exactly equal to k

arr = list(map(int,input("Enter the elements :").split()))

K = int(input("The value of K is :"))

count = 0 


for i in arr:
    if i == K :
        count += 1 

print(count) 


