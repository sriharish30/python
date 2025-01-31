a=int(input("enter the salary:"))
b=int(input("enter the age:"))
if(a>=20000 or b<=25):
    loan=int(input("enter loan amount:"))
    if(loan<=50000):
        print("you are eligible for loan")
    else:
        print("maximum loan amount is 50000")
else:
    print("you are not eligible for loan ")