#la universidad desea clasificar a los estudiantes por la estatura y recomendar
#un deporte
#si la estatura es menor de 1.50 se recomienda ajedrez
#si la estatura es entre 1.50 y 1.70 se recomienda futbol
#si es mayor a 1.70 basket
#se desea un reporte que diga la cantidad y el % de estudiante por deporte
#de cada deporte se desea un reporte de cantidad de mujeres y hombre con %
acumAjedrez = 0
acumFutbol = 0
acumBasket = 0
MujeresA = 0
HombresA = 0
MujeresF = 0
HombresF = 0
MujeresB = 0
HombresB = 0

cant = int(input("Cantidad de estudiantes: -> "))

cont = 1
while cont <= cant:
    estatura = float(input("Ingrese estatura del estudiante " + str(cont) + ": "))
    
    if estatura < 1.50:
        acumAjedrez += 1
        genero = input("Ingrese género del estudiante " + str(cont) + " (mujer/hombre): ")
        if genero == "mujer":
            MujeresA += 1
        elif genero == "hombre":
            HombresA += 1
    
    elif estatura <= 1.70:
        acumFutbol += 1
        genero = input("Ingrese género del estudiante " + str(cont) + " (mujer/hombre): ")
        if genero == "mujer":
            MujeresF += 1
        elif genero == "hombre":
            HombresF += 1

    else:
        acumBasket += 1
        genero = input("Ingrese género del estudiante " + str(cont) + " (mujer/hombre): ")
        if genero == "mujer":
            MujeresB += 1
        elif genero == "hombre":
            HombresB += 1
    cont += 1


porcAjedrez=(acumAjedrez/cant)*100
porcFutbol=(acumFutbol/cant)*100
porcBasket=(acumBasket/cant)*100


if acumAjedrez > 0:
    porcMujeresA=(MujeresA/acumAjedrez)*100
    porcHombresA=(HombresA/acumAjedrez)*100
else:
    porcMujeresA = porcHombresA = 0

if acumFutbol > 0:
    porcMujeresF=(MujeresF/acumFutbol)*100
    porcHombresF=(HombresF/acumFutbol)*100
else:
    porcMujeresF = porcHombresF = 0

if acumBasket > 0:
    porcMujeresB=(MujeresB/acumBasket)*100
    porcHombresB=(HombresB/acumBasket)*100
else:
    porcMujeresB = porcHombresB = 0


print("Reporte de estudiantes por deporte:")
print("Cantidad estudiantes de Ajedrez: " + str(acumAjedrez) + " Porcentaje: " + str(round(porcAjedrez, 2)) + "%")
print("Cantidad estudiantes de Fútbol: " + str(acumFutbol) + " Porcentaje: " + str(round(porcFutbol, 2)) + "%")
print("Cantidad estudiantes de Basket: " + str(acumBasket) + " Porcentaje: " + str(round(porcBasket, 2)) + "%")

print("\nReporte de género por deporte:")
print("Ajedrez - Mujeres: " + str(MujeresA) + " (" + str(round(porcMujeresA, 2)) + "%), Hombres: " + str(HombresA) + " (" + str(round(porcHombresA, 2)) + "%)")
print("Fútbol - Mujeres: " + str(MujeresF) + " (" + str(round(porcMujeresF, 2)) + "%), Hombres: " + str(HombresF) + " (" + str(round(porcHombresF, 2)) + "%)")
print("Basket - Mujeres: " + str(MujeresB) + " (" + str(round(porcMujeresB, 2)) + "%), Hombres: " + str(HombresB) + " (" + str(round(porcHombresB, 2)) + "%)")
