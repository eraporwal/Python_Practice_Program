#slicing
i="i am Mayank Runija"
x=i[3:5]
y=i[6:9]
z=i[ :9]
print(i)
print(x)
print(y)
print(z)
print("\n")

#splitng
a=i.split(" ")
print(a)
print("\n")

#concatenation
c="mayank"
d="runija"
print(c+" "+d)
print("\n")

#Multiplication
mul=3*c
print(mul)
star="*"
q=1*star
w=2*star
e=3*star
print(q+"\n"+w+"\n"+e)

#star pattern with loop
num=int (input("Enter no of stars : "))
for i in range(num+1):
    print (i*"*")
