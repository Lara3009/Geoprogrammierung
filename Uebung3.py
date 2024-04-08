import math

class Punkt:
    def __init__(self,x,y):
        self.x = x
        self.y = y

#------------------------------------

class Figur:
    def __init__(self):
        self.name = "Figur"

    def Umfang(self):
        return 0

    def __str__(self):
        return self.name


class Dreieck(Figur):
    def __init__(self, Punkt1,Punkt2,Punkt3):
        super().__init__()
        self.a = Punkt1
        self.b = Punkt2
        self.c = Punkt3

    def Umfang(self):
        return 
    
    def __str__(self):
        return self.name

class Rechteck(Figur):
    def __init__(self,Punkt4,Punkt5):
        super().__init__()
        self.d = Punkt4
        self.e = Punkt5
        self.name = "Rechteck"
    
    def Umfang(self):
        return 2* abs(d.x -e.x) + 2*(d.y-e.y)
    
    def __str__(self):
        return self.name

class Kreis(Figur):
    def __init__(self,mittelpunkt, radius):
        super().__init__()
        self.M = mittelpunkt
        self.r = radius
        self.name = "Kreis"

    def Umfang(self):
        return self.r*2*math.pi
    
    def __str__(self):
        return self.name

    
k = Kreis(Punkt(0,0),10)
print(k.name,k.Umfang())

recht = Rechteck((3,4),(5,9))
print(recht.name,recht.Umfang())
