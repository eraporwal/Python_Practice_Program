n=10
for i in range (n):
    print(i)

print("next")
for i in range (1,n+1):
    print(i)


print("next")
for i in range(2,21,2):
    print(i)

print("next")
a=int(input("Enter A Number :"))
m=a*10
count=1
for i in range(a,m+1,a):
    print(a,"*",count,"=",i)
    count=count+1

