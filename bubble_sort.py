
arr = list(map(int,input("Enter elements with a space to be sorted : ").split()))


n = len(arr)

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("The sorted arrray is as follows ")

print(arr)

