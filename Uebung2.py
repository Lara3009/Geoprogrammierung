class Vector3:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
    
    def len(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return Vector3(self.x + other, self.y + other, self.z + other)
        else:
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        
    def __radd__(self, other):
        return Vector2(self.x + other, self.y + other, self.z + other)

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            return Vector3(self.x - other, self.y - other, self.z - other)
        else:
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        
    def __rsub__(self, other):
        return Vector3(self.x - other, self.y - other, self.z - other)
    
    def __mul__(self,other):
        if type(other) == int or type(other) == float:
            return Vector3(self.x * other, self.y * other, self.z * other)
        else:
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
    
    def __rmul__(self,other):
        return Vector3(self.x * other, self.y * other, self.z * other)

    def dot(self,other):
        return (self.x * other.x + self.y * other.y + self.z * other.z)
    
    def cross(self,other):
        return Vector3(self.y*other.z -self.z*other.y,self.z*other.x -self.x*other.z,self.x*other.y - self.y*other.x)

    def norm(self):
        Betrag = (self.x**2 + self.y**2 + self.z**2)**0.5
        return Vector3(self.x*(1/Betrag),self.y*(1/Betrag),self.z*(1/Betrag))
#----------------------------------------------------------------

a = Vector3(3,4,2)
b = Vector3(2,1,0)
Summe = a + b
Diverenz = a-b
Produkt = a*b
Produkt2 =  2 * a
Produkt3 = a * 2
d = a.dot(b)
e = a.cross(b)

print(str(a))
print(a.len())
print(Summe)
print(Diverenz)
print(Produkt)
print(Produkt2)
print(Produkt3)
print(d)
print(e)
print(a.norm())