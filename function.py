def fact(n):
    fact_n=1
    for i in range (1,n+1):
        fact_n *= i
    return (fact_n)
    
x=int(input("enter total : "))
y=int(input("enter value : "))
fx=fact(x)
fy=fact(x-y)
p=fx/fy
print("permutation is = ",p)