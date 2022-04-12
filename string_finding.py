str1="i am fine "
x=len(str1)
for i in range(x):
    print("{} is at index {}".format(str1[i],i))
    
    
#finding index form character
# Y=str1.index("character")
y=str1.index("i")
print(y)
#finding index form character and print it in a loop
for i in str1:
    print(str1.index(i))

#printing in reverce order
for i in range(x-1,-1.-1):
    print(i)