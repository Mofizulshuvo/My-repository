#There is common algorithms for finding GCD !
def GCD(a,b):
        r=a%b
        while r!=0:
            a=b
            b=r
            r=a%b
        return b
    
print("Enter Numbers:")
x=int(input())
y=int(input())

z= GCD(x,y)
print(f"GCD of {x} & {y} is : {z}")