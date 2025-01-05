# Definir el diccionario con personas
personal = {
    "persona1": {"nombre": "saya", "edad": 23, "genero": "f", "profesion": "Ingeniero"},
    "persona2": {"nombre": "pepe", "edad": 87, "genero": "m", "profesion": "Medico"},
    "persona3": {"nombre": "andrea", "edad": 32, "genero": "f", "profesion": "enfermera"}
}

# Imprimir el diccionario completo
print(personal)

# Función para mostrar las claves del diccionario principal
for clave in personal.keys():
    print(clave)

# Función para mostrar nombres específicamente
for datos in personal.values():
    print(datos["nombre"])

# Función para mostrar todos los datos
for datos in personal.values():
    nom = datos["nombre"]
    eda = datos["edad"]
    gen = datos["genero"]
    pro = datos["profesion"]
    print(f"{nom} {eda} {gen} {pro}")

# Añadir empresas al diccionario
personal["empresas"] = ["ucc", "movistar", "kfc"]

# Imprimir el diccionario con los nuevos datos
print(personal)
