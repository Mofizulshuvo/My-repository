import string 
def PuncRemove(x):
    y=x.maketrans("","",string.punctuation)
    z= x.translate(y)
    return z

a=input("write some thing : ")
r=PuncRemove(a)
print(r)