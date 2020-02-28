import re
import json
from datetime import datetime
import sqlite3
try:
 
  #texto = """
  #buscate largo texto extenso
  #largo largo 
  #largo
  #"""
  #resultado = re.findall("largo",texto)
  #print(resultado)
  #print("encontrado " + str(len(resultado)) + " en texto")
  #print(re.split("\n",texto))

  producto = {
    "item":"001",
    "color":"rojo",
    "valor":"1200"
    }
  prodJson = json.dumps(producto)
  #print(prodJson)
  prodDic = json.loads(prodJson)
  #print(prodDic)
  #fyh = datetime.now()
  listaPersonas = [('Sebastian','Parra',27),('Benjamin','Parra',27),('Catalina','Fuentes',31)]
  conexion = sqlite3.connect("datos.db")
  cursor = conexion.cursor()
  #cursor.execute("CREATE TABLE personas(nombre TEXT, apellido TEXT, edad INTEGER)")
  #cursor.execute("insert into personas values('juan','parra',27)")
  #cursor.executemany("insert into personas values(?,?,?)",listaPersonas)

  cursor.execute("select * from personas")
  personas = cursor.fetchall()

  for persona in personas:
    print(persona)

  # cursor.execute("delete from personas where nombre = 'juan'")


  # conexion.commit()
  conexion.close()

except Exception as e:
  print("error")
  print(e)
 