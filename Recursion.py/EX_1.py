'''
✅ Q1. Print Numbers from 1 to N
Input: n = 5
Output: 1 2 3 4 5

You must use recursion, not a loop.

'''
def nums_1_to_n (n):
    if n == 0 :
     return 
    nums_1_to_n(n-1)
    print(n)

nums_1_to_n(5)    