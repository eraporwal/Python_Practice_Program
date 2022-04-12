a=input("enter your name : ")
str_=""
for i in range(len(a)-1,-1,-1):
    str_=str_+a[i]
print(str_)

b=input("enter your name : ")[::-1]

print(b)


