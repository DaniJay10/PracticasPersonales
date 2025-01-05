import numpy as np
import matplotlib.pyplot as plt

# Datos de ventas en millones para primer y segundo semestre
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
ventas_1er_semestre = [1235, 5600, 8000, 7000, 5800, 12000]
ventas_2do_semestre = [10500, 9500, 8500, 7200, 6000, 14000]

# Añadimos las ventas del segundo semestre para tener las 12
ventas_totales = ventas_1er_semestre + ventas_2do_semestre

# Gráfica combinada: Barras para el primer semestre, línea para el segundo semestre
fig, ax1 = plt.subplots()

# Índices para las barras
ind = np.arange(len(meses))

# Graficar barras para el primer semestre
ax1.bar(ind[:6], ventas_1er_semestre, width=0.6, color='skyblue', label="1er Semestre")

# Crear el segundo eje Y para la línea del segundo semestre
ax2 = ax1.twinx()

# Graficar línea para el segundo semestre
ax2.plot(ind[6:], ventas_2do_semestre, color='green', marker='o', label="2do Semestre")

# Etiquetas y título
ax1.set_xlabel("Meses")
ax1.set_ylabel("Ventas 1er Semestre (millones)")
ax2.set_ylabel("Ventas 2do Semestre (millones)")
plt.title("Comparación de Ventas Semestrales")

# Ajustar los nombres de los meses en el eje X
ax1.set_xticks(ind)
ax1.set_xticklabels(meses, rotation=45)

# Leyendas para ambos ejes
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")

# Mostrar la gráfica
plt.tight_layout()
plt.show()
