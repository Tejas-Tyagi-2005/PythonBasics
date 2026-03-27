# Write a function that takes a string  
# and returns the reversed string

def string_reverser(s):
    rev = ""
    for i in s:
        rev = i + rev 
    return rev 

print(string_reverser("aidnI"))    


    

