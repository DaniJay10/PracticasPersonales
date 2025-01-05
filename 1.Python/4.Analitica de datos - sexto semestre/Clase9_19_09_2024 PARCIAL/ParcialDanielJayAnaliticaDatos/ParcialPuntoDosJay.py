#Parcial Daniel Andres Pinzon Jay ID:819793 punto 2
import matplotlib.pyplot as plt
import numpy as np
a=int(input("Digite valor de a "))
b=int(input("Digite valor de b "))
c=int(input("Digite valor de c "))
discriminante = b**2 - 4*a*c
if discriminante >= 0 and a!= 0:
    x1 = (-b+np.sqrt(discriminante))/(2*a)  # Primera solución
    x2 = (-b-np.sqrt(discriminante))/(2*a)  # Segunda solución
    print(f"Las soluciones son: x1 = {x1}, x2 = {x2}")
    Xmin = min(x1, x2)-5
    Xmax = max(x1, x2)+5
    x = np.linspace(Xmin, Xmax, 400)
    y = a*x**2 + b*x + c  
    plt.plot(x, y)
    #diseño:
    plt.axhline(0, color='black')  #dibujar una linea horizontal. El 0 es la posicion en Y 
    plt.axvline(0, color='black')  #dibuja una linea vertical. El 0 es la posicion en X
    plt.title(f"Gráfico de la ecuación cuadrática: y = {a}x^2 + {b}x + {c}")
    plt.scatter([x1, x2], [0, 0], color='blue')#scatter muestra datos como puntos
    plt.grid(True)#crea una cuadricula
    plt.show()

else:
    print("El ejercicio no tiene soluciones reales")
