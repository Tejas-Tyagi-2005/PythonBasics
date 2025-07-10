#Calculates factorial of a number using loop


num = int(input("Enter a number to calculate its factorial :"))

# factorial formula  = num! = num * (num -1) * (num -2) * ...* 1 


result = 1 

for i in range(1 , num +1 ):
    result = result * i 
    


print("The factorial of ", num, "is" , result)
