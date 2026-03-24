# Count how many elements lie strictly between L and R (L < i < R)

arr = list(map(int,input("Enter the elements :").split()))

L = int(input(" Value of L :"))

R = int(input("Value of R "))


count = 0 

for i in arr:
    if i> L and i< R :
        count += 1 

print(count) 

