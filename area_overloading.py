print("Program for area's overloading")
class area:
    def area(self, *x):
        ar=0
        if(len(x)==0):
            ar="no value passed"
        elif(len(x)==1):
            ar=3.14*x[0]*x[0]
        elif(len(x)==2):
            ar=x[0]*x[1]
        else:
            ar="Illegal number of inputs"
        return ar
fig=area()
r=int(input("enter radius:"))
print("Area of circle is:",fig.area(r))

l=int(input("enter length:"))
b=int(input("enter breadth:"))
print("Area of Rectangle is:",fig.area(l,b))