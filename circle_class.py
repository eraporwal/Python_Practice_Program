class circle :
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    def circumference(self):
        return 2*3.14*self.radius

rad=circle(int(input("\nEnter Radius of Circle : ")))
print("\nArea of circle is : ",rad.area())
print("Circumference of circle is : ",rad.circumference())