


def div(x,y):
    if x<y:
        x,y=y,x
    return x/y

a=int(input("Enter Value of A : "))
b=int(input("Enter Value of B : "))
c=div(a,b)
print("Value of C is : ",c)
