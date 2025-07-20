def longest_common_prefix (strs):
    if not strs :
        return ""
    
    prefix = ""


    for i in range(len(strs[0])):
        char = strs[0][i]
        for words in strs[1:]:
            if i >= len(words) or words[i] != char:
                return prefix 
        prefix = prefix + char 


user_input = input("Enter strings seperated by spaces :")
strs = user_input.strip().split()


result = longest_common_prefix(strs)
print("the longest common prefix is :", result)