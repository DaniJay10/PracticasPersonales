#Parcial Daniel Andres Pinzon Jay ID:819793 punto 1
import matplotlib.pyplot as plt
temperaturas=[]
dias=[]
Ntemp = int(input("¿Cuántas temperaturas deseas ingresar? "))
for i in range(Ntemp):
    
    temp = float(input(f"Digite la temperatura {i+1}: "))
    temperaturas.append(temp)
    dia = int(input(f"Digite el día correspondiente a la temperatura {i+1}: "))
    dias.append(dia)


#grafica de lineas
plt.plot(dias, temperaturas, marker='o')
plt.title("Temperatura (°C) por dia")
plt.ylabel("Temperatura (°C)")
plt.xlabel("Dia")
plt.show() 

#grafica de lineas
plt.bar(dias,temperaturas,color="blue")
plt.title("Temperatura (°C) por dia")
plt.xlabel("Dia")
plt.ylabel("Temperatura (°C)")
plt.show()

#despues de abierto el grafico de lineas, favor cerrar para abrir el de barras
