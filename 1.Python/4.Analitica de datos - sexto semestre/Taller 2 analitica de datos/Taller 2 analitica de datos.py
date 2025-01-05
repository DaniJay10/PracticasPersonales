import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
#PUNTO 1
data = {
    'Date': ['2021-01-05', '2021-01-12', '2021-02-20', '2021-03-15', '2022-01-08', '2022-04-10','2022-05-22', '2022-07-19', '2023-03-15', '2023-05-27', '2023-09-12'],
    'Store ID': [1, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1],
    'Product ID': [1001, 1002, 1003, 1004, 1005, 1006, 1002, 1007, 1008, 1009, 1010],
    'Category': ['Electrónica', 'Ropa', 'Hogar', 'Electrónica', 'Alimentos', 'Ropa','Electrónica', 'Hogar', 'Electrónica', 'Alimentos', 'Ropa'],
    'Customer ID': ['C001', 'C002', 'C001', 'C003', 'C002', 'C003', 'C001', 'C004', 'C002', 'C001', 'C004'],
    'Sales Amount': [250.00, 120.00, 300.00, 500.00, 80.00, 150.00, 600.00, 320.00, 700.00, 95.00, 200.00],
    'Units Sold': [1, 2, 3, 1, 4, 2, 1, 2, 1, 5, 3]
}
#convercion del formato fecha
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

#PUNTO 2
df['Year-Month'] = df['Date'].dt.to_period('M')  
meses_ventas = df.groupby('Year-Month')['Sales Amount'].sum()
plt.figure(figsize=(10, 6))
meses_ventas.plot(kind='line', marker='o', color='b')
plt.title('Punto 2: Evolución de las Ventas Mensuales (2021-2023)')
plt.xlabel('Fecha')
plt.ylabel('Total de Ventas')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
#hallar manualmente mes con mas y menos ventas
mes_mayor_ventas = meses_ventas.idxmax()  
mayor_ventas = meses_ventas.max()  
mes_menor_ventas = meses_ventas.idxmin() 
menor_ventas = meses_ventas.min()  
print(f"Mes con mayor volumen de ventas: {mes_mayor_ventas} (${mayor_ventas:.2f})")
print(f"Mes con menor volumen de ventas: {mes_menor_ventas} (${menor_ventas:.2f})")

#PUNTO 3

df['Year'] = df['Date'].dt.year

categoria_year = df.groupby(['Year', 'Category'])['Sales Amount'].sum().unstack()
categoria_year.plot(kind='bar', figsize=(10, 6))
plt.title('Punto 3: Comparación de Ventas por Categoría en Diferentes Años')
plt.ylabel('Monto Total de Ventas')
plt.xlabel('Año')
plt.xticks(rotation=0)
plt.show()

#PUNTO 4
df['Month'] = df['Date'].dt.month
plt.figure(figsize=(10, 6))
for year in df['Year'].unique():
    datos_year = df[df['Year'] == year]
    plt.plot(datos_year['Month'], datos_year['Sales Amount'], marker='o', label=f'Año {year}')
plt.xticks(ticks=range(1, 13), labels=['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])
plt.title('Punto 4: Ventas Individuales por Mes y Año')
plt.ylabel('Monto de Venta')
plt.xlabel('Mes')
plt.grid(True)
plt.legend(title='Año', loc='upper left')
plt.tight_layout()
plt.show()


#PUNTO 5
# Productos más vendidos
productos_vendidos = df.groupby('Product ID')['Sales Amount'].sum().sort_values(ascending=False)
top_3_productos = productos_vendidos.head(3)
print("Top 3 productos más vendidos:")
print(top_3_productos.rename_axis('Product ID').reset_index(name='Total Sales'))

# Clientes más recurrentes
clientes_recurrentes = df['Customer ID'].value_counts()
print("Clientes más recurrentes:")
print(clientes_recurrentes.rename_axis('Customer ID').reset_index(name='Frequency'))


df_top_productos = df[df['Product ID'].isin(top_3_productos.index)]
ventas_acumuladas = df_top_productos.groupby([df_top_productos['Date'].dt.year, 'Product ID'])['Sales Amount'].sum().unstack()
ventas_acumuladas.plot(kind='bar', stacked=True)
plt.title('Punto5: Ventas Acumuladas de los 3 Productos Más Vendidos (2021-2023)')
plt.ylabel('Monto Total de Ventas')
plt.xlabel('Año')
plt.xticks(rotation=0)
plt.legend(title='Product ID')
plt.tight_layout()  
plt.show()

#PUNTO 6
meses_ventas = df.groupby('Year-Month')['Sales Amount'].sum().reset_index()
meses_ventas['Year'] = meses_ventas['Year-Month'].dt.year
meses_ventas['Month'] = meses_ventas['Year-Month'].dt.month
meses_ventas['Time'] = meses_ventas['Year'] + (meses_ventas['Month'] - 1) / 12
X = meses_ventas[['Time']]  
y = meses_ventas['Sales Amount']
modelo = LinearRegression()
modelo.fit(X, y)
tiempo2024 = np.arange(2024, 2025, 1/12).reshape(-1, 1)  
compras_2024 = modelo.predict(tiempo2024)
plt.figure(figsize=(10, 6))
plt.plot(meses_ventas['Time'], meses_ventas['Sales Amount'], label='Ventas Reales', marker='o')
plt.plot(tiempo2024, compras_2024, label='Predicciones 2024', linestyle='--', color='red', marker='x')


plt.xticks(ticks=range(2021, 2025), labels=['2021', '2022', '2023', '2024'])
plt.title('Punto 6: Predicción de Ventas Mensuales para 2024')
plt.xlabel('Año')
plt.ylabel('Monto de Venta')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



