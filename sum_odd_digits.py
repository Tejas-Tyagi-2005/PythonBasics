# Given a number (no spaces), find the sum of all odd digits

num = input()

total = 0 

for i in num:
    if int(i)%2 != 0:
        total += int(i)
print(total)

