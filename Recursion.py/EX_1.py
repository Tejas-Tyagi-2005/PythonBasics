def nums_1_to_n (n):
    if n == 0 :
     return 
    nums_1_to_n(n-1)
    print(n)

nums_1_to_n(5)