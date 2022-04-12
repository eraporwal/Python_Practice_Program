print("program for file handling")

f=open("my_first_file.txt","w")
f.write("Jay Shree Ram!!!!!!!!!")
f.write("\n")
x=("My name is Mayank")
f.write(x)
f.close()

f=open("my_first_file.txt","r")
y=f.read()
print(y)
f.close()