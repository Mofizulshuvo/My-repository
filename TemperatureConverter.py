#Temperature Converter

def TempConvertor(n):
    if n==1:
        C=float(input("Enter The Celsius value : "))
        F=(C*(float(9/5)))+32
        print(f"The Farenheit value of {C} Celsius is : {F}")
    
    elif n==2:
        C=float(input("Enter The Celsius value : "))
        K= (C+273)
        print(f"The Kelvin value of {C} Celsius is : {K}")
    
    elif n==3:
        F=float(input("Enter The Farenheit value : "))
        C= (F-32)*float(5/9)
        print(f"The Celsius value of {F} Farenheit is : {C}")
    
    elif n==4:
        F=float(input("Enter The Farenheit value : "))
        C=(F-32)*float(5/9)
        K= C+273
        print(f"The Kelvin value of {F} Farenheit is : {K}")
    
    elif n==5:
        K=float(input("Enter The Kalvin value : "))
        C= (K-273)
        print(f"The Celsius value of {K} Kelvin is : {C}")
    
    elif n==6:
         K=float(input("Enter The Kalvin value : "))
         C=(K-273)
         F=(C*(float(9/5)))+32
         print(f"The Farenheit value of {K} Kelvin is : {F}")
    
    else:
        print("You Entered a wrong number!")
        
    
print("Temperater Converter:\n")
while True:
 x=int(input("Press '1' to convert Celsius To Farenheit\nPress '2' to convert Celsius To Kelvin\nPress '3' to convert Farenheit To Celsius \nPress '4' to convert Farenheit To Kelvin \nPress '5' to convert Kelvin To Celsius \nPress '6' to convert Kelvin To Farenheit \n"))    
 TempConvertor(x)
 print("\n")

        
        