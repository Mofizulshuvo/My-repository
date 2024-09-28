def swap(a,b):
   t=a
   a=b
   b=t
   return a,b

x=int(input("Enter First number : "))
y=int(input("Enter Second number : "))
print(f"Before swapping :\nFirst Number is {x} & Second Number {y}")

x,y=swap(x,y)
print(f"After swapping :\nFirst Number is {x} & Second Number {y}")