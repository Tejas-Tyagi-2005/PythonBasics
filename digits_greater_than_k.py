# Given a number (no spaces), print all digits greater than k

num = input()

k = int(input("Enter value of k :"))

for i in num:
    if int(i)>k:
        print(int(i))

        