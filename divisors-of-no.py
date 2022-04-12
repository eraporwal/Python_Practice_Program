#divisors of a number

no=int(input("Enter a Number for finding factors : "))
for i in range(1,no+1):
    if(no%i==0):
        print(i)
    
    