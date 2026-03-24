# Count how many numbers in the array lie between two values L and R (inclusive)

arr = list(map(int,input("Enter elements :").split()))

count = 0 

L = int(input("Enter value of L : "))

R = int(input("Enter value of R : "))

for i in arr:
    if i>= L and i<= R:
        count += 1

print(count)