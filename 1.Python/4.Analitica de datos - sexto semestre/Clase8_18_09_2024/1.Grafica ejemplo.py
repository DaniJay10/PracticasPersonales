import matplotlib.pyplot as plt  # Importa el módulo para hacer gráficos

# y = x^2
x = [0, 1, 2, 3, 4, 5]  # Lista de valores de X
y = [0, 1, 4, 9, 16, 25]  # Lista de valores de Y (y = x^2)

plt.plot(x, y)  # Grafica los puntos X e Y
plt.title("FUNCIÓN Y=X^2")  # Agrega un título al gráfico
plt.xlabel("X")  # Etiqueta del eje X
plt.ylabel("Y")  # Etiqueta del eje Y
plt.show()  # Muestra el gráfico
