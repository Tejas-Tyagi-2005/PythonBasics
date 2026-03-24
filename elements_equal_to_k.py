# Print all elements in the array that are equal to k

arr = list(map(int,input("Enter the elements :").split()))


k = int(input("The value of k is :"))

for i in arr:
    if i == k:
        print(i)


 
        