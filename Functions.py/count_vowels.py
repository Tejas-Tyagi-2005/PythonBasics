# Write a function that takes a string  
# and returns the number of vowels (a, e, i, o, u)

def vowel_return(letters):
    count = 0 
    letters = letters.lower()
    for i in letters:
        if i in "aeiou":
            count += 1
        

    return count 




print(vowel_return("python"))

