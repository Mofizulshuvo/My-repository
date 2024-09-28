import random
def RandomFloat(a,b):
    ranfloat=random.uniform(a,b)
    print(f"The random float value of the range {a} to {b} is = {ranfloat}")
def RandomIntiger(a,b):
    ranint=random.randint(a,b)
    print(f"The random integer Number of the range {a} to {b} is = {ranint}")    
    
print("Enter the range for the random float number")
x=float(input("Lower range : "))
y=float(input("Upper range : "))
RandomFloat(x,y)
print("\nEnter the range for the random integer number")
a=int(input())
b=int(input())
RandomIntiger(a,b)