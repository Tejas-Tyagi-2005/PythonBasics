# Given a number (no spaces), find the sum of digits strictly between L and R (L < digit < R)


num = input()

L = int(input("Value of L :"))

R = int(input("Value of R  :"))


count = 0 


for i in num:
    if int(i)>L and int(i)<R :
        count += i

print(count)        