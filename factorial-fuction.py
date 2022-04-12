
print("Program for factorial of number ")
def fact(x):
    if(x==0 or x==1):
        y=1
        return (y)
    else:
        y=x*fact(x-1)
        return (y)
val=int(input("Enter a value : "))
funct_val=fact(val)
print("factorial of {} is {} ".format(val,funct_val))