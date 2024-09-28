def largest(a,b,c):
    if a>=b and a>=c :
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
    
a=int(input("Enter first  Number  : "))
b=int(input("Enter second Number  : "))
c=int(input("Enter third  Number  : "))
l=largest(a,b,c)
print(f"largest one is : {l} ")
