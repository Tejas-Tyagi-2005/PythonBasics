# Given a number (no spaces), find the sum of digits less than k

num = input()


k = int(input("Enter the value of k :"))


total = 0 

for i in num:
    if int(i)<k:
        total += int(i)

print(total)       
