import pandas as pd

data = {
    "Producto": ["Producto A", "Producto B", "Producto C", "Producto D", "Producto E"],
    "Fecha": ["2024-01-01", "2024-01-03", "2024-02-01", "2024-02-03", "2024-03-05"],
    "Cantidad": [10, 20, 30, 25, 10],
    "Precio": [10, 20, 30, 25, 10],
    "Categorias": ["Ferretería", "Aseo", "Eléctrica", "Ferretería", "Eléctrica"]
}


print(" datos del diccionario ")
print("*********************")
print(data)

#Convertir el diccionario 'data' en un DataFrame de pandas
print(" datos del DataFrame ")
print("*********************")
df = pd.DataFrame(data)#Un DataFrame es una estructura de datos bidimensional, similar a una tabla.
print(df)

#Convertir la columna 'Fecha' de tipo string a formato de fecha (datetime)
print(" datos del DataFrame (con fecha type DateTime ")
print("*********************")
df["Fecha"]=pd.to_datetime(df['Fecha'])#'pd.to_datetime' convierte las fechas en un formato adecuado para operaciones con fechas
print(df)

#agregar columna ventas
print("  datos del DataFrame con Ventas  ")
print("*********************")
df["Ventas"] = df["Cantidad"] * df["Precio"]  # Nueva columna 'Ventas' con el total de ventas por cada producto.
print(df)

#calcular ventas por producto
print("*********************")
print(" Ventas totales por producto  ")
print("*********************")
venta_por_producto = df.groupby("Producto")["Ventas"].sum().reset_index()
venta_por_producto.columns = ["Producto", "Ventas Totales"]# Agrupa por 'Producto' y suma las ventas totales por producto.
print(venta_por_producto)


#calcular ventas totales por categoria
print("*********************")
print("  Ventas totales por categoria  ")
print("*********************")
venta_por_categoria = df.groupby("Categorias")["Ventas"].sum()
print(venta_por_categoria)

#calcular ventas totales pormes
print("*********************")
print("  Ventas totales por mes  ")
print("*********************") 
ventas_por_mes = df.resample('ME', on='Fecha')["Ventas"].sum() #resample en pandas es utilizado para reorganizar o transformar datos de series temporales a una frecuencia especificada.
print(ventas_por_mes)


#Producto mas vendido
print("*********************")
print("  Producto mas vendido  ")
print("*********************")
pro_mas_vendido=df.groupby("Producto")["Ventas"].sum().idxmax()
pro_mas_vendido_v=df.groupby("Producto")["Ventas"].sum().max()
print(pro_mas_vendido," ---> ", pro_mas_vendido_v)









