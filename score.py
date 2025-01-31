a=int(input("enter the score:"))
if(a<35):
    print("poor student")
elif(a>35 and a<70):
    print("average student")
elif(a>70 and a<=100):
    print("good student")
else:
    print("invalid input")