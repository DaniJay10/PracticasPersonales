#la universidad desea hacer un programa que de los N estudiantes del salon
#imprimir el promedio de las n notas que el profesor saca a cada estudiante
# en su curso.
#imprimir el promedio del curso
def calcular_promedio(suma_notas, num_notas):
    return suma_notas / num_notas

def validar_nota(nota):
    if 0 <= nota <= 5:
        return True
    else:
        print("Nota inválida. Debe estar entre 0 y 5.")
        return False

n = int(input("Ingrese el número de estudiantes: "))
suma_total_promedios = 0
promedio_mas_alto = 0
estudiante_con_mayor_promedio = 0

for i in range(n):
    print("\nEstudiante " + str(i + 1) + ":")
    num_notas = int(input("Ingrese el número de notas: "))
    suma_notas = 0
    
    for j in range(num_notas):
        while True:
            nota = float(input("Ingrese la nota " + str(j + 1) + ": "))
            if validar_nota(nota):
                break
        suma_notas += nota
    
    promedio = calcular_promedio(suma_notas, num_notas)
    suma_total_promedios += promedio
    print("El promedio del estudiante " + str(i + 1) + " es: " + str(round(promedio, 2)))
    
    if promedio > promedio_mas_alto:
        promedio_mas_alto = promedio
        estudiante_con_mayor_promedio = i + 1


promedio_curso = suma_total_promedios / n
print("\nEl promedio del curso es: " + str(round(promedio_curso, 2)))


print("El promedio más alto es: " + str(round(promedio_mas_alto, 2)) +
      " y lo obtuvo el estudiante " + str(estudiante_con_mayor_promedio))
