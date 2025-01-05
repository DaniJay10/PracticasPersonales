import matplotlib.pyplot as plt
import numpy as np
a=int(input("Digite valor de a"))
b=int(input("Digite valor de b"))
c=int(input("Digite valor de c"))
discriminante = b**2 - 4*a*c
if discriminante >= 0 and a!= 0:
    r1 = (-b + np.sqrt(discriminante)) / (2*a)  # Primera solución
    r2 = (-b - np.sqrt(discriminante)) / (2*a)  # Segunda solución
    print(f"Las soluciones son: r1 = {r1}, r2 = {r2}")
    x = np.linspace(-10, 10, 100)  
    y = a * x**2 + b * x + c  
    plt.plot(x, y)

    plt.axhline(0, color='black',linewidth=1)  # Línea horizontal
    plt.axvline(0, color='black',linewidth=1)  # Línea vertical
    plt.title("Gráfico de la ecuación cuadrática")
    plt.show()

else:
    print("El ejercicio no tiene solucion")


