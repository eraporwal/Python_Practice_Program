a=int(input("Enter 1st value :"))
b=int(input("Enter 2nd value :"))
c=int(input("Enter 3rd value :"))

if(a==b==c):
    print("All values are equal")
elif(a==b<c):
    print("A & B values are equal and smaller than C")
elif(a==b>c):
    print("A & B values are equal and grater than C")
elif(a>b==c):
    print("B & C values are equal and smaller than A")
elif(a<b==c):
    print("B & C values are equal and grater than A")
elif(b>c==a):
    print("A & C values are equal and smaller than B")
elif(b<c==a):
    print("A & C values are equal and grater than B")
elif(a>b)and (a>c):
    print(a, "is Maximum")
elif (b>c):
    print(b, "is Maximum")
else:
    print(c, "is Maximum")
    if (a<b) and (a<c):
        print(a, " is Manimum")
    elif (b<c):
        print(b, "is Manimum")
    else:
        print(c, "is Manimum")

