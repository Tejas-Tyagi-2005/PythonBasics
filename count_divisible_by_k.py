# Count how many numbers in the array are divisible by k


arr = list(map(int,input("Enter elements :").split()))


K = int(input("The value of K is .....:"))


count = 0 


for i in arr:
    if i%K == 0:
        count += 1 

print(count) 


