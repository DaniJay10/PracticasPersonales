import matplotlib.pyplot as plt

meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']
ventas = [1235, 5600, 8000, 7000, 5800, 12000]


plt.plot(meses, ventas, marker='o')

plt.title("Ventas Semestrales (en millones)")
plt.xlabel("Meses")
plt.ylabel("Ventas (millones)")


plt.show()
