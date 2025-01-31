a=int(input("enter the  first number:"))
b=int(input("enter the  second number:"))
operations=input("add/sub/mul/div:")
if(operations=="add"):
    print(a+b)
elif(operations=="sub"):
    print(a-b)
elif(operations=="mul"):
    print(a*b)
elif(operations=="div"):
    print(a/b)
else:
    print("invalid operations")


