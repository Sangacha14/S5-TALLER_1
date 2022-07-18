class Empresa:
    def __init__(self,ruc, nombre, telf, dirc, correo):
        self.ruc = ruc
        self.razonsocial = nombre
        self.telf = telf
        self.dirc = dirc
        self.correo = correo

if __name__ == "__main__":
    emp1 = Empresa("0453927952", "Somos más", "0835363232", "Milagro", "josd@hotmail.com")
    emp2 = Empresa("0434534543", "Somos menos", "0834389232", "Durán", "jodfsdf@hotmail.com")
    print(emp1.razonsocial, emp1.ruc)
    print(emp2.razonsocial, emp2.ruc)