#program for leap year

leap=int(input("enter a year : "))
if((leap%100==0) and (leap%400==0)):
    print("it is a leap year")
elif((leap%4==0) and (leap%100!=0)):
    print("it is a leap year")
else:
    print("not")