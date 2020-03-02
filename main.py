from entidades.persona import persona
from clases.crud import crudClass

class programa:

  def __init__(self):
    self.crud = crudClass()
    self.saludos()

  def saludos(self):
    print("Buenos días buenas tardes")
    print("en que lo puedo ayudar")
    self.menu()

  def menu(self):
    print("Selecciones una opcion")
    print("1.- Listar")
    print("2.- Agregar")
    print("3.- Eliminar")
    print("4.- Actualizar")
    opcion = input()
    #print(opcion == "1")
    if(opcion == "1"):
      self.crud.select()
  
  


prog = programa()

#crudClass.select()

# miPersona = persona('sebaaaa', 'Parrita', 27)
# myCrud = crudClass()
# myCrud.insertar(miPersona)
# myCrud.select()
# print("==================")
# miNewPersona = persona('sebiwi', 'Parrita', 27)

# myCrud.delete(miNewPersona)
# #myCrud.update(miPersona, miNewPersona)
# myCrud.select()
