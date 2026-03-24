# Print all elements in the array that lie strictly between L and R (L < i < R)

arr = list(map(int,input("enter the elements :").split()))

L = int(input(" Value of L :"))

R = int(input("Value of R "))

for i in arr:
    if i>L and i<R :
        print(i)

        