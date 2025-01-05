# Importar las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generar datos aleatorios
np.random.seed(0)  # Para obtener resultados consistentes
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

color = np.random.rand(100)
size = 100 * np.random.rand(100)

# Crear la gráfica
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Dibujar el scatter plot en 3D
sc = ax.scatter(x, y, z, c=color, s=size, alpha=0.7, cmap='viridis')

# Añadir etiquetas
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

# Añadir barra de colores
plt.colorbar(sc)

# Mostrar la gráfica
plt.show()
