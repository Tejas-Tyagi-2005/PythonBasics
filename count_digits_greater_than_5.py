# Given a number (no spaces), count how many digits are greater than 5

arr = input("Enter the number :")

count = 0 

for i in arr:
    if int(i) > 5:
        count += 1 

print(count)
