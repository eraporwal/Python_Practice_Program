# to take details name,contact,email
info=["aaditya" ,123, "ad123@","IIPS,DAVV"]
print(info)
print("name :",info[0])
print("number : ",info[1])
print("email :",info[2])
print("college :",info[3])

print("************by loop")
for i in info:
    print(i),

#length of list
a=[1,2,3,4,5,6,7,8,9]
x=len(a)
for i in range(x):
    print(a[i])
#find index by value
print(info.index("aaditya"))
