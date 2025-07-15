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

## noon --- len is 4 mid is 2 (len/2) (sarting from position 1 and 2 starting from position 4)
## racecar --- len is 7 mid is 4 ((len+1)/2) (starting from position 1 upto 4 and starting from posiiton 7 upto 4)
'''
def palindrome2(word: str):
    n = len(word)
    mid = 0;
    if(len%2==0): ## Even Number. Mid is n/2
        mid = n/2
    else:
        mid = (n+1)/2

    i = 1 , j = n
    while((i <= mid) and (j>=mid)):
        if(word[i] != word[j]):
            print("Not a Palindrome")
            break
        i=i+1
        j=j-1
    else:
        print("Is a Palindrome")

    


'''