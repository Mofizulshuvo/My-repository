def reverse(x):
    reversenum=0
    
    while x>0:
        rem=x%10
        reversenum=(reversenum*10)+rem
        x=int(x/10)
    return reversenum

x=int(input("Enter a number : "))   
y=reverse(x)     
print(f"Reverse Number is : {y}")
    
    