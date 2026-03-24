# Count how many numbers are even and how many are odd


arr = list(map(int,input("check how many nums even or odd : ").split()))


Even = 0

Odd = 0

for i in arr:
    if i%2 == 0:
        Even += 1
    else :
        Odd += 1


print("Even :" , Even)

print("Odd : " ,Odd)