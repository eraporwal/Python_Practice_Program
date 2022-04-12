#program for prime number

no=int(input("enter a digit for check prime number : "))
if (no>1):
    for i in range(2,no):
        if((no%i)==0):
         print(no,"is not a prime number!!!")
         break
    else:
        print(no,"is a prime number!!!")
else:
    print(no,"is not a prime number!!!")

 