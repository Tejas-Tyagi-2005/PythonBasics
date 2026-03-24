# Find the sum of all elements in the array that are less than k


arr = list(map(int,input("Enter the elements :").split()))

k = int(input("Enter the value of k :"))

total = 0 


for i in arr:
    if i < k :
        total += i 

print(total)


