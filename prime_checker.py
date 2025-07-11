# Ask the user to enter a number and check whether it is a prime number or not.
# Print "Prime" if it is, else print "Not Prime".

num = int(input("Enter a number to check if it is prime or not :"))


if num<= 1 :
    print("Et numero non primo")
else:
    for i in range(2 , num ):
        if num % i == 0 :
            print("et numero non primo")
            break
    else:

      print("et numero e primo")
