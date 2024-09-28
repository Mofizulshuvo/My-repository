def fibonacci(x):
    if x<=0:
        print("Enter a positive number")
    else:    
     first=0
     second=1
     for _ in range(x):
      print(first,end=" ")
      next=first+second
      first=second
      second=next
n=int(input("Enter a number : "))
fibonacci(n)     
      
      
     
         
        