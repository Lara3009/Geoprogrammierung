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
    

#----------------------------------------------------------------

a = Vector3(3,4,2)
b = Vector3(2,1,0)
Summe = a + b
Diverenz = a-b
Produkt = a*b
Produkt2 =  2 * a
Produkt3 = a * 2


print(str(a))
print(a.len())
print(Summe)
print(Diverenz)
print(Produkt)
print(Produkt2)
print(Produkt3)