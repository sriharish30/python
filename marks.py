a=int(input("enter the tamil mark:"))
b=int(input("enter the english mark:"))
c=int(input("enter the maths mark:"))
d=int(input("enter the science mark:"))
e=int(input("enter the social mark:"))
f=(a+b+c+d+e)/5
print(f)
if(f<35):
    print("additional class is required")
else:
    print("you are good to go")