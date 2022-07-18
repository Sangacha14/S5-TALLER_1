from abc import ABC, abstractclassmethod

class Usuario(ABC):
  def __init__(self,nombre, cedu, telefono, email, direccion, idRol):
    self.nombre = nombre
    self.cedula = cedu
    self.telf = telefono
    self.correo = email
    self.dirc = direccion
    self.idRol =idRol
  
  @abstractclassmethod
  def validarCedula(self):
    pass

  def mostrarUsuario(self):
    print ("Usuario: {} {} {} {} {} {}".format(self.nombre, self.cedula, self.telf, self.correo, self.dirc, self.idRol))
  