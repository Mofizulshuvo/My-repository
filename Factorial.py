def Factorial(n):
    if n==0:
        return 1
    else:
        while n!=0:
         F=n*Factorial(n-1)
         return F  
    
n=int(input("Enter The Number : "))    
F=Factorial(n)
print(f"The Factorial of {n} is {F}")