def vowelcount(x):
    vowel="aeiou"
    x=x.lower()
    p=x.replace(" ","")
    count=0
    for i in x:
       if i in vowel:
           count=count+1
    print(f"Total vowel = {count}")        
        
x=input("Enter sentence of word : ")
vowelcount(x)