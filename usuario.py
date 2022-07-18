class Usuario:
  def __init__(self, nombre, cedu, telefono, email, direccion, idRol):
    self.nombre = nombre
    self.cedula = cedu
    self.telf = telefono
    self.correo = email
    self.dirc = direccion
    self.idRol =idRol
  
  def mostrarUsuario(self):
    print ("Usuario: {} {} {} {} {} {}".format(self.nombre, self.cedula, self.telf, self.correo, self.dirc, self.idRol))
   
  def validarCedula(self):
    if len(self.cedula == 10):
      return self.cedula
    else:
      return "999999999"

class Cliente(Usuario):
  def __init__(self, nombre, cedu, telefono, email, direccion, idRol, estado=False):
    super().__init__(nombre, cedu, telefono, email, direccion, idRol) 
    self.estado = estado
  
  def mostrarUsuario(self):
    estado = "Estado: Activo" if self.estado else "Estado: Inactivo"
    super().mostrarUsuario()
    print("{}".format(estado))
    
class Coach(Usuario):
  def __init__(self, nombre, cedu, telf, correo, dirc, idRol, estado=False):
    super().__init__(nombre, cedu, telf, correo, dirc, idRol)
    self.estado = estado

  def mostrarUsuario(self):
    estado ="Estado: Activo" if self.estado else "Estado: Inactivo"
    super().mostrarUsuario()
    print("{}".format(estado))
    #print("Usuario: {} {} {} {} {} {} {}".format(self.nombre, self.cedula, self.telf, self.correo, self.dirc, self.idRol, self.estado))
    
if __name__ == "__main__":
    usu= Coach("Denn", "0929608511", "0990255359","dmorang5@unemi.edu.ec","Milagro", "123", True)
    usu.mostrarUsuario()