# Find the sum of all elements in the array that lie between L and R (inclusive)

arr = list(map(int,input("Enter the elements :").split()))


total = 0 

L = int(input("Enter value of L :"))

R = int(input("Enter value of R "))


for i in arr:
    if i>= L and i<= R:
        total += i 

print(total)



