from support import *
def smart_div(func):
    def inner(m,n):
        if(m<n):
            m,n=n,m
        return func(m,n)
    return inner

a=int(input("Enter Value of A : "))
b=int(input("Enter Value of B : "))
c=div(a,b)
div1=smart_div(div)
d = div1(a,b)
print("Value of C is : ",c)

print("a = ",a)
print("b = ",b)
print("c = ",c)
print("d = ",d)