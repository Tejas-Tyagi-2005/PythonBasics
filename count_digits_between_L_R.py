# Given a number (no spaces), count how many digits lie between L and R (inclusive)


num = input()


L = int(input("Enter value of L : "))

R = int(input("Enter value of R : "))

count = 0 

for i in num:
    if int(i)>=L and int(i)<=R:
        count += 1 
print(count)


