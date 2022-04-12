#calculator!!!!!! 
# take 2 user defind value , 
# 5 choices for arithmetic operation , 
# float or integer,
# create functions for each operation

print("Welcome to calculator!!!!!!!!")

inp=int(input("Enter 1 for interger datatype \nEnter 2 for float datatype : "))
opr=input("Enter which arithmetic operation you want to perform ( + , - , * , / , % ) : ")
a=input("Enter 1st value : ")
b=input("Enter 2nd value : ")
if(inp==1):
    a=int(a)
    b=int(b)
elif(inp==2):
    a=float(a)
    b=float(b)
else:
    print("invalid input ")

def sum(a,b):
    c=a+b
    print("sum of a and b is : ",c)
    return(c)
def sub(a,b):
    c=a-b
    print("substraction of a and b is : ",c)
    return(c)
def mul(a,b):
    c=a*b
    print("mul of a and b is : ",c)
    return(c)
def div(a,b):
    c=a/b
    print("division of a and b is : ",c)
    return(c)
def mod(a,b):
    c=a%b
    print("modules of a and b is : ",c)
    return(c)

if(opr=="+"):
    c=sum(a,b)
elif(opr=="-"):
    c=sub(a,b)
elif(opr=="*"):
    c=mul(a,b)
elif(opr=="/"):
    if(b==0):
        print("invalid input divion by 0 is not defind")
        
    c=div(a,b)
elif(opr=="%"):
    if(b==0):
        print("invalid input divion by 0 is not defind")
        
    c=mod(a,b)
else:
    print("invalid operation")

    

