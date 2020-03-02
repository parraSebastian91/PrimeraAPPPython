import sqlite3
from entidades.persona import persona


class crudClass:
    def __init__(self):
        try:
            self.conexion = sqlite3.connect("datos.db")
        except Exception as e:
            print("no se puede conectar a la DB, Error:{}" + e)
        else:
            print("Conexion OK")

    def insertar(self, person):
        cursor = self.conexion.cursor()
        cursor.execute(
            "insert into personas(nombre,apellido,edad) values('{}','{}',{})".
            format(person.nombre, person.apellido, person.edad))
        self.conexion.commit()

    def select(self):
        cursor = self.conexion.cursor()
        cursor.execute("select * from personas")
        personas = cursor.fetchall()
        for person in personas:
            print(person)

    def delete(self, person):
        cursor = self.conexion.cursor()
        cursor.execute("delete from personas where nombre = '{}'".format(
            person.nombre))
        self.conexion.commit()

    def update(self, oldPeson, newPerson):
        cursor = self.conexion.cursor()
        query = "update personas set nombre = '{}' , apellido = '{}',edad = {} where nombre = '{}'".format(newPerson.nombre, newPerson.apellido, newPerson.edad, oldPeson.nombre)
        cursor.execute(query)
        self.conexion.commit()

    def cerrarConexion(self):
        self.conexion.close()