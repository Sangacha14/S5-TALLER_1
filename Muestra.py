from empresa import Empresa
from usuario import Cliente, Coach
from interface import RutinaCoach
# import os

# print("Información")
# emp1 = Empresa("0929608511", "El Hoy", "0990255359", "Milagro", "dmorang5@unemi.edu.ec")
# print ("Empresa: {}  -  {}".format(emp1.ruc, emp1.razonsocial))
# usu = Cliente("Denn", "0929608511", "0990255359","dmorang5@unemi.edu.ec", "Milagro", "123",True)
# usu.mostrarUsuario
class Detalle:
  _NumeroR = 0
  def __init__(self, rutina,tiempo, serie):
    Detalle._NumeroR += 1
    self.linea = Detalle._NumeroR
    self.rutina = rutina
    self.tiempo = tiempo
    self.serie = serie

class Mostrar: 
  _NumeroR = 0
  def __init__(self, usuario, rol):
    Detalle._NumeroR += 1
    self.usuario = usuario
    self.rol = rol
    # self.rutina = rutina
    # self.tiempo = tiempo
    # self.serie = serie
    self.detalleR = []
  
  def agregarDetalle(self, rutinas, tiempos, series):
    detalle = Detalle(rutinas,tiempos,series)
    self.detalleR.append(detalle)

  def mostrarInfo(self, empNom, empRuc):
    print("Empresa: {:17} Ruc:{}".format(empNom, empRuc))
    self.usuario.mostrarUsuario()
    print("Rol: {}".format(self.rol))
    print("✦"*20,"Lista de rutinas","✦"*20)
    print("NumeroR    Ejercicio         Tiempo        Serie")
    for det in self.detalleR:
      print("{:7} {:16} {:10} {:5}".format(det.linea, det.rutina, det.tiempo, det.serie))


if __name__ == "__main__":
  emp1= Empresa("0929608511", "El Hoy", "0990255359", "Milagro", "dmorang5@unemi.edu.ec")
  usu = Cliente("Denn", "0929608511", "0990255359", "dmorang5@unemi.edu.ec", "Milagro", "124", True)
  usua = Coach("Denn", "0929608511", "0990255359", "dmorang5@unemi.edu.ec", "Milagro", "123", False)
  mos = Mostrar(usua, "Coach")
  nombre =input("Ingrese nombre de rutina: ")
  tiempo =input("Ingrese tiempo de rutina: ")
  serie =input("Ingrese serie de rutinas: ")
  # usu = RutinaCoach()
  # usu.añadirRutina(nombre, tiempo, serie)
  mos.agregarDetalle(nombre, tiempo, serie)
  mos.agregarDetalle("mancuernas", "20 minutos", "4 series")
  mos.agregarDetalle("sentadillas", "20 minutos", "4 series")
  mos.mostrarInfo(emp1.razonsocial, emp1.ruc)