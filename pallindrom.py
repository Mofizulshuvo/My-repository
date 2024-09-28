
def palindrom(s):
    p=s.replace(" ","")
    q=p.lower()

    if q==q[::-1]:
     print("This item is a pallyndrom")
    else:
     print("This item is not Pallyndrom")

     
x=input("Enter a word or sentence : ")

palindrom(x)