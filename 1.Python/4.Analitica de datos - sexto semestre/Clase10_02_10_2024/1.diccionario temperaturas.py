# Lista de días de la semana
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Diccionario para almacenar las temperaturas
temperaturas = {}

# Pedir al usuario las temperaturas para cada día
for dia in dias_semana:
    # Preguntar cuántas temperaturas se van a ingresar para ese día
    cantidad = int(input(f"¿Cuántas temperaturas vas a ingresar para {dia}? "))
    
    # Crear una lista para almacenar las temperaturas de ese día
    temperaturas_dia = []
    
    # Pedir al usuario cada temperatura y añadirla a la lista
    for i in range(cantidad):
        temp = float(input(f"Ingresa la temperatura {i+1} para {dia}: "))
        temperaturas_dia.append(temp)
    
    # Asignar la lista de temperaturas al diccionario con el día como clave
    temperaturas[dia] = temperaturas_dia

# Mostrar el diccionario de temperaturas
print("\nTemperaturas registradas por día de la semana:")
for dia, temp in temperaturas.items():
    print(f"{dia}: {temp}")
