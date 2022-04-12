print("class for phone book")

class contact:
    def __init__(self,name,address,phone_no):
            self.name=name
            self.phone_no=phone_no
            self.address=address
    def postdata(self):
            f=open("phone.txt","a")
            pno=str(self.phone_no)
            p1=[self.name,self.address,pno]
            for i in range(0,len(p1)):
                f.write(p1[i])
                f.write(",")
            f.close()
def getdata():
    f=open("phone.txt","r")
    l=f.read()
    f.close()
    return l

name1=input("Please enter the name:")
addr1=input("Please enter the address:")
no1=int(input("Please enter the number:"))
p=contact(name1,addr1,no1)
p.postdata()
l=getdata()
print("data is :\n")
l1=l.split(",")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
print("NAME   |   ADDRESS   |   NUMBER")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
n=1
for i in l1:
    if(n<3):
        print("|",i," ",end="")
        n+=1
    else:
        print("|",i,"\n")
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
        n=1






# class contact :
#     def __init__(self,name,contact_number,home_address):
#         self.name=name
#         self.contact_number=contact_number
#         self.home_address=home_address
    
#     def putdata(self):
#         f=open("phone.txt","a")
#         nm=str([self.name])
#         f.write(nm)
#         pnum=str([self.contact_number])
#         f.write(pnum)
#         addr=str([self.home_address])
#         f.write(addr)
#         f.close()



# p1_name=input("Enter Your Name : ")
# p1_number=int(input("Enter Your contact number : "))
# p1_addr=input("Enter Your address : ")
# p=contact(p1_name,p1_number,p1_addr)
# p.putdata()  
# print("_ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ _ ")
# print("Name  |   Contact  |   Address")
# print("_ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ _ ")
# print(p.putdata())
# print("_ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ __ _ _ ")



# def getdata():
#         f=open("phone.txt","r")
#         data=f.read()
#         f.close()
#         return data
# file_p=getdata()
# print("data is  : ",file_p)


