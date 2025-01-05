vigilante = {
    "vigilante1":  {"nombre": "Paco", "edad": 28, "genero": "M"},
    "vigilante2":  {"nombre": "Maria", "edad": 37, "genero": "F"},
    "vigilante3":  {"nombre": "Juan", "edad": 23, "genero": "M"},
    "vigilante4":  {"nombre": "Rosa", "edad": 42, "genero": "F"}
}


suma_edades = 0

# Recorrer el diccionario y sumar las edades
for datos in vigilante.values():  
    edad = datos["edad"]
    suma_edades += edad


promedio = suma_edades/len(vigilante)

# Imprimir el promedio de las edades
print("El promedio de las edades es:", promedio)
