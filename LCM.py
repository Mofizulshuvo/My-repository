#LCM of two numbers
#We know, If we multify two numbers and then divide the result of multification 
# by the GCD of those two numbers.Then we get the LCM 

#Function For GCD
def GCD(a,b):
        r=a%b
        while r!=0:
            a=b
            b=r
            r=a%b
        return b

#Function for LCM
def LCM(a,b):
    x=(a*b)//(GCD(a,b))

    return x


A=int (input("Enter first  Number : "))
B=int (input("Enter second Number : "))

C=LCM(A,B)
print(f"The LCM of {A} and {B} is : {C}")
