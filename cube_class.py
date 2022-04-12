class cube:
    def __init__(self,side):
        self.side=side
    def volume(self):
        return(self.side*self.side*self.side)  
    def Surface_area(self):
        return(6*self.side*self.side)
    def Lateral_Surface_area(self):
        return(4*self.side*self.side)

are=cube(int(input("Enter the Area of One Side : ")))
print("\nVolume of Cube is : ",are.volume())
print("\nSurface Area of Cube is : ",are.Surface_area())
print("\nLateral Surface Area of Cube is : ",are.Lateral_Surface_area())