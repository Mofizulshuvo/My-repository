def sumofseqnum(a):
    sum=(a*(a-1))/2
    return sum

n=int(input("Enter Number : "))
sum=sumofseqnum(n)
print(f"The sum of first {n} number is : {sum}")