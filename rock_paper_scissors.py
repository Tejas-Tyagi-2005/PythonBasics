# Build a simple Rock-Paper-Scissors game.
# User inputs their choice, and computer randomly picks one.
# Print who wins the game.

import random 

user_choice = str(input("choose either rock , paper or sissors :"))

sys_choice = random.choice(['rock','paper','sissors'])

if user_choice not in  ['rock','paper','sissors']:
    print("Please choose from the given options .Make sure to type the correct spelling")
else:
    print('I chose - '+sys_choice)
    print ('You chose - '+user_choice)
    if sys_choice == 'rock' and user_choice == 'paper' :
      print("congratulations , you win ")


    elif sys_choice == 'paper' and user_choice == 'rock':
      print("Sorry , you lost")


    elif sys_choice == 'sissors' and user_choice == 'paper':
      print("sorry , you lost ")    


    elif sys_choice == 'paper' and user_choice == 'sissors':
      print("congratulations  you win ")


    elif   sys_choice == user_choice :
     print("Try again its a draw ")
    
    
 

    
     


















    


