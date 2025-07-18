def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = ""

    for i in range(len(strs[0])):
        char = strs[0][i]
        for word in strs[1:]:
            if i >= len(word) or word[i] != char:
                return prefix
        prefix += char

    return prefix

user_input = input("Enter words separated by space: ")
strs = user_input.strip().split()

result = longest_common_prefix(strs)
print("Longest common prefix:", result)
