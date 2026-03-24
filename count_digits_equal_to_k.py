# Given a number (no spaces), count how many digits are equal to k

num = input()

k = int(input("Enter the value of k :"))
count = 0 


for i in num:
    if int(i) == k:
        count += 1 


print(count)        