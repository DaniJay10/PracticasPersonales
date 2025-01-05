vigilante = {
    "nombre": [],
    "edad": []
}


while True:
    respuesta = input("¿Desea ingresar un vigilante? (y/n): ").lower()
    if respuesta == 'y':
        nombre = input("Ingrese el nombre del vigilante: ")
        vigilante["nombre"].append(nombre)
        edad = int(input("Ingrese la edad del vigilante: "))
        vigilante["edad"].append(edad)
    elif respuesta == 'n':
        break
    else:
        print("Respuesta no válida.")

if len(vigilante["edad"]) > 0:
    promedio = sum(vigilante["edad"])/len(vigilante["edad"])
    print("El promedio de edad es:",promedio)
else:
    print("No se ingresaron vigilantes.")
