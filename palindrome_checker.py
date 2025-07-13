# Ask the user to enter a string or number and check whether it is a palindrome.
# Print "Palindrome" if it is, else print "Not Palindrome".

print("\n palindrome refers to a string or number that is exactly the same when reversed , Ex - 121 = 121 , and Bob = Bob \n")
print("\nThis programm checks if the input , is a palindrome .\n \nEx - Nitin is a palindrome ,  Rohit is not \n ")
user_str = input("Enter a string to check if it is a palindrome :")

palindrome_check = user_str[::-1]

if palindrome_check == user_str :
    print("The string you entered is a palindrome ")
else :
    print("the string you entered is not a palindrome ")
