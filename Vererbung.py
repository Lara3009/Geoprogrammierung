class Tier:
    def __init__(self, name,anzahlBeine):
        self.name = name
        self.anzahlBeine = anzahlBeine

    def essen(self):
        print("mjam")

    def schlafen(self):
        print("zzzzhh")

class Hund(Tier):
    def __init__(self):
        super().__init__("Hund",4)

    def schlafen(self):
        print("zzzh,wuff,zzzh,wuff")

class Katze(Tier):
    def __init__(self):
        super().__init__("Katze",4)

    def schlafen(self):
        print("zzzh,Miau,zzzh,miau")

bello = Hund()
stella = Katze()

print(bello.anzahlBeine)
bello.schlafen()
bello.essen()

stella.schlafen()
stella.essen()