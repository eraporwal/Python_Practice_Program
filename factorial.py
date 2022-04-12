num =int(input("Enter a Number for calculate factorial : "))
fac = 1
if num < 0:
   print("factorial not exist")
elif num==0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
    fac = fac*i
   print("The factorial of",num,"is",fac)
