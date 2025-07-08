#User keeps guessing a random number until correct


user_num  = int(input("Guess a number between 1 and 10  :"))

import random

from matplotlib.pylab import rand
rand_num = random.randint(1, 10)

while user_num != rand_num :
    if user_num < rand_num :
        print("Too low , try again ")
    else :
        print("Too high ,try again ")
    user_num = int(input("Guess a number between 1 and 10  :"))
print("Congratulations! You guessed the number correctly.")



