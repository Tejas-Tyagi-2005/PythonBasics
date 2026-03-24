# Given a number (no spaces), count how many digits are even

num = input()

count = 0 

for i in num:
    if int(i)%2 == 0 :
        count += 1 

print(count) 

