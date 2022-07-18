class Rutina():
  def añadirRutina(self):
    pass
  def mostrarRutina(self):
    pass
 
class RutinaCoach():
  def añadirRutina(self, nombre, tiempo, serie):
    print("✦"*20,"Ingreso de rutinas","✦"*20)
    self.nombre = nombre
    self.tiempo = tiempo
    self.serie = serie
    # self.nombre =input("Ingrese nombre de rutina: ")
    # self.tiempo =input("Ingrese tiempo de rutina: ")
    # self.serie =input("Ingrese serie de rutinas: ")
  def mostrarRutina(self):
    print("✦"*20,"Rutinas ingresadas","✦"*20)
    return("Rutinas: {} Tiempo: {} Series: {}".format(self.nombre, self.tiempo, self.serie))

class RutinaCliente():
  def mostrarRutina(self):
    print("✦"*20,"Rutinas ingresadas","✦"*20)
    return("Rutinas: {} Tiempo: {} Series: {}".format(self.nombre, self.tiempo, self.serie))

if __name__ == "__main__":
  usu = RutinaCoach()
  usu.añadirRutina()
  usu.mostrarRutina()