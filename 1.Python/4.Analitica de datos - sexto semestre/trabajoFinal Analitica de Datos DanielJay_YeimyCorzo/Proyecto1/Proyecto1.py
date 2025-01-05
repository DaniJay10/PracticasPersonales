import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import os
#Daniel Andres Pinzon Jay
#Yeimy Tatiana Corzo Lizarazo
# 1. Cargar y leer datos
def cargar_datos(archivo):
    print("\n--- Datos del archivo ---")
    df = pd.read_csv(archivo, delimiter='\t')
    print(df.head(10).to_string(index=False)) 
    return df

# 2. Estructurar datos con listas y diccionarios
def estructurar_datos(df):
    transacciones = df.values.tolist()
    ventas_por_producto = {}
    ventas_por_region = {}

    for transaccion in transacciones:
        producto = transaccion[1]
        region = transaccion[4]
        total_venta = transaccion[5]

        if producto not in ventas_por_producto:
            ventas_por_producto[producto] = 0
        ventas_por_producto[producto] += total_venta

        if region not in ventas_por_region:
            ventas_por_region[region] = 0
        ventas_por_region[region] += total_venta

    print("\n--- Estructuración Completa ---")
    return transacciones, ventas_por_producto, ventas_por_region

# 3. Analisis de datos
def total_ventas_por_producto_region(transacciones, ventas_por_producto, ventas_por_region):
    print("\n--- Lista de Transacciones ---")
    print("{:<12} {:<12} {:<10} {:<15} {:<12} {:<10}".format("Fecha", "Producto", "Cantidad", "Precio Unitario", "Región", "Total Venta"))
    for transaccion in transacciones:
        print("{:<12} {:<12} {:<10} {:<15} {:<12} ${:<10.2f}".format(
            transaccion[0], transaccion[1], transaccion[2], transaccion[3], transaccion[4], transaccion[5]))

    print("\n--- Total de Ventas por Producto ---")
    for producto, total in ventas_por_producto.items():
        print(f"{producto}: ${total:.2f}")

    print("\n--- Total de Ventas por Región ---")
    for region, total in ventas_por_region.items():
        print(f"{region}: ${total:.2f}")

def promedio_ventas(df, imprimir=True):
    df['fecha_venta'] = pd.to_datetime(df['fecha_venta'], format='%d/%m/%Y')
    promedio_diario = df.groupby(df['fecha_venta'].dt.date)['total_venta'].mean()
    promedio_mensual = df.groupby(df['fecha_venta'].dt.to_period('M'))['total_venta'].mean()

    if imprimir:
        print("\n--- Promedio de Ventas Diarias ---")
        for fecha, promedio in promedio_diario.items():
            print(f"{fecha}: ${promedio:.2f}")

        print("\n--- Promedio de Ventas Mensuales ---")
        for mes, promedio in promedio_mensual.items():
            print(f"{mes}: ${promedio:.2f}")

    return promedio_diario, promedio_mensual


def productos_extremos(ventas_por_producto):
    max_ventas = max(ventas_por_producto, key=ventas_por_producto.get)
    min_ventas = min(ventas_por_producto, key=ventas_por_producto.get)
    
    print("\n--- Productos Más Vendido y Menos Vendido ---")
    print(f"Más vendido: {max_ventas} (${ventas_por_producto[max_ventas]:.2f})")
    print(f"Menos vendido: {min_ventas} (${ventas_por_producto[min_ventas]:.2f})")

def tendencias_estacionales(df):
    df['fecha_venta'] = pd.to_datetime(df['fecha_venta'], format='%d/%m/%Y', dayfirst=True)
    df['mes'] = df['fecha_venta'].dt.month
    ventas_mensuales = df.groupby('mes')['total_venta'].sum()
    promedio_mensual = ventas_mensuales.mean()
    indices_estacionales = ventas_mensuales / promedio_mensual

    texto_indices = "--- Índice estacional x mes ---\n"
    for mes, ventas in ventas_mensuales.items():
        texto_indices += f"Mes {mes}: ${ventas:.2f} - Índice Estacional: {indices_estacionales[mes]:.2f}\n"

    mes_pico = ventas_mensuales.idxmax()
    mes_bajo = ventas_mensuales.idxmin()
    texto_indices += f"\nMes con mayor venta: {mes_pico} (${ventas_mensuales[mes_pico]:.2f})\n"
    texto_indices += f"Mes con menor venta: {mes_bajo} (${ventas_mensuales[mes_bajo]:.2f})\n"
    
    plt.figure(figsize=(12, 6))
    plt.plot(ventas_mensuales.index, ventas_mensuales.values, marker='o', color='b', label="Ventas Mensuales")
    plt.axhline(y=promedio_mensual, color='r', linestyle='--', label="Promedio Mensual")
    plt.xlabel("Mes")
    plt.ylabel("Total Ventas")
    plt.title("Ventas Mensuales y Tendencias Estacionales")
    plt.xticks(range(1, 13))
    plt.legend()
    plt.grid()
    filename = "tendencias_estacionales.png"
    plt.savefig(filename)
    plt.close()

    return texto_indices, filename
#debido a un problema que no supeimos solucionar existe una funcion de indices estacionales para registrar en el pdf y otra para mostrar al usuario por consola.
def tendencias_estacionales_mostrar(df):
    df['fecha_venta'] = pd.to_datetime(df['fecha_venta'], format='%d/%m/%Y', dayfirst=True)
    df['mes'] = df['fecha_venta'].dt.month

    ventas_mensuales = df.groupby('mes')['total_venta'].sum()
    promedio_mensual = ventas_mensuales.mean()
    indices_estacionales = ventas_mensuales / promedio_mensual

    print("\n--- Ventas Mensuales para Identificar Tendencias Estacionales ---")
    for mes, ventas in ventas_mensuales.items():
        print(f"Mes {mes}: ${ventas:.2f} - Índice Estacional: {indices_estacionales[mes]:.2f}")

    mes_pico = ventas_mensuales.idxmax()
    mes_bajo = ventas_mensuales.idxmin()
    print(f"\nMes con mayor venta: {mes_pico} (${ventas_mensuales[mes_pico]:.2f})")
    print(f"Mes con menor venta: {mes_bajo} (${ventas_mensuales[mes_bajo]:.2f})")

    plt.figure(figsize=(12, 6))
    plt.plot(ventas_mensuales.index, ventas_mensuales.values, marker='o', color='b', label="Ventas Mensuales")
    plt.axhline(y=promedio_mensual, color='r', linestyle='--', label="Promedio Mensual")
    plt.xlabel("Mes")
    plt.ylabel("Total Ventas")
    plt.title("Ventas Mensuales y Tendencias Estacionales")
    plt.xticks(range(1, 13))
    plt.legend()
    plt.grid()
    plt.show()

# 3. Graficas de datos
#debido a un fallo que no supimos como solucionar cada grafica va a tener dos funciones una para ser insertada en el informe y otra para ser mostrada cuando el usuario lo pida (opcion5,6,7)
def grafica_distribucion_ventas(ventas_por_producto):
    productos = list(ventas_por_producto.keys())
    total_ventas = list(ventas_por_producto.values())

    plt.figure(figsize=(10, 6))
    plt.bar(productos, total_ventas, color='skyblue')
    plt.xlabel("Producto")
    plt.ylabel("Total Ventas")
    plt.title("Distribución de Ventas por Producto")
    plt.xticks(rotation=45)
    filename = "grafico_distribucion_ventas.png"
    plt.savefig(filename)
    plt.close()
    return filename

def grafica_distribucion_ventas_mostrar(ventas_por_producto):
    productos = list(ventas_por_producto.keys())
    total_ventas = list(ventas_por_producto.values())

    plt.figure(figsize=(10, 6))
    plt.bar(productos, total_ventas, color='skyblue')
    plt.xlabel("Producto")
    plt.ylabel("Total Ventas")
    plt.title("Distribución de Ventas por Producto")
    plt.xticks(rotation=45)
    plt.show()
    
def grafica_evolucion_ventas(df):
    df['fecha_venta'] = pd.to_datetime(df['fecha_venta'], format='%d/%m/%Y', dayfirst=True)
    fechas = df['fecha_venta']
    ventas = df['total_venta']

    plt.figure(figsize=(12, 6))
    plt.plot(fechas, ventas, marker='o', color='coral')
    plt.xlabel("Fecha")
    plt.ylabel("Total Ventas")
    plt.title("Evolución de las Ventas a lo Largo del Tiempo")
    plt.xticks(rotation=45)
    plt.grid()
    filename = "grafico_evolucion_ventas.png"
    plt.savefig(filename)
    plt.close()
    return filename

def grafica_evolucion_ventas_mostrar(df):
    df['fecha_venta'] = pd.to_datetime(df['fecha_venta'], format='%d/%m/%Y', dayfirst=True)
    fechas = df['fecha_venta']
    ventas = df['total_venta']

    plt.figure(figsize=(12, 6))
    plt.plot(fechas, ventas, marker='o', color='coral')
    plt.xlabel("Fecha")
    plt.ylabel("Total Ventas")
    plt.title("Evolución de las Ventas a lo Largo del Tiempo")
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

def grafica_comparacion_productos_regiones(ventas_por_producto, ventas_por_region):
    productos = list(ventas_por_producto.keys())
    total_ventas_productos = list(ventas_por_producto.values())

    regiones = list(ventas_por_region.keys())
    total_ventas_regiones = list(ventas_por_region.values())

    fig, axs = plt.subplots(1, 2, figsize=(14, 6))

    # Ventas por producto
    axs[0].bar(productos, total_ventas_productos, color='skyblue')
    axs[0].set_title("Ventas por Producto")
    axs[0].set_xlabel("Producto")
    axs[0].set_ylabel("Total Ventas")
    axs[0].tick_params(axis='x', rotation=45)

    # Ventas por región
    axs[1].bar(regiones, total_ventas_regiones, color='lightgreen')
    axs[1].set_title("Ventas por Región")
    axs[1].set_xlabel("Región")
    axs[1].set_ylabel("Total Ventas")
    axs[1].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    filename = "grafico_comparacion_productos_regiones.png"
    plt.savefig(filename)
    plt.close()
    return filename

def grafica_comparacion_productos_regiones_mostrar(ventas_por_producto, ventas_por_region):
    productos = list(ventas_por_producto.keys())
    total_ventas_productos = list(ventas_por_producto.values())

    regiones = list(ventas_por_region.keys())
    total_ventas_regiones = list(ventas_por_region.values())

    fig, axs = plt.subplots(1, 2, figsize=(14, 6))

    # Ventas por producto
    axs[0].bar(productos, total_ventas_productos, color='skyblue')
    axs[0].set_title("Ventas por Producto")
    axs[0].set_xlabel("Producto")
    axs[0].set_ylabel("Total Ventas")
    axs[0].tick_params(axis='x', rotation=45)

    # Ventas por región
    axs[1].bar(regiones, total_ventas_regiones, color='lightgreen')
    axs[1].set_title("Ventas por Región")
    axs[1].set_xlabel("Región")
    axs[1].set_ylabel("Total Ventas")
    axs[1].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.show()
    
# 5. Reportes e interactividad    
def generar_informe_pdf(nombre_archivo, ventas_por_producto, ventas_por_region, promedio_diario, promedio_mensual, max_ventas, min_ventas, df):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Informe de Análisis de Ventas", 0, 1, "C")
    pdf.ln(10)
    #ventas x producto
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Ventas por Producto", 0, 1)
    pdf.set_font("Arial", "", 10)
    for producto, total in ventas_por_producto.items():
        pdf.cell(0, 10, f"{producto}: ${total:.2f}", 0, 1)
    #ventas x region
    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Ventas por Región", 0, 1)
    pdf.set_font("Arial", "", 10)
    for region, total in ventas_por_region.items():
        pdf.cell(0, 10, f"{region}: ${total:.2f}", 0, 1)
   #promedio ventas diarias 
    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Promedio de Ventas Diarias", 0, 1)
    pdf.set_font("Arial", "", 10)
    for fecha, promedio in promedio_diario.items():
        pdf.cell(0, 10, f"{fecha}: ${promedio:.2f}", 0, 1)
    #promedio ventas mensuales 
    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Promedio de Ventas Mensuales", 0, 1)
    pdf.set_font("Arial", "", 10)
    for mes, promedio in promedio_mensual.items():
        pdf.cell(0, 10, f"{mes}: ${promedio:.2f}", 0, 1)

    pdf.ln(5)
    pdf.cell(0, 10, f"Producto más vendido: {max_ventas}", 0, 1)
    pdf.cell(0, 10, f"Producto menos vendido: {min_ventas}", 0, 1)

       
    # Generar las gráficas 
    grafico_1 = grafica_distribucion_ventas(ventas_por_producto)
    pdf.image(grafico_1, x=10, y=pdf.get_y() + 10, w=180)
    pdf.ln(80)
    os.remove(grafico_1)  

    grafico_2 = grafica_evolucion_ventas(df)
    pdf.image(grafico_2, x=10, y=pdf.get_y() + 10, w=180)
    pdf.ln(80)
    os.remove(grafico_2)  

    grafico_3 = grafica_comparacion_productos_regiones(ventas_por_producto, ventas_por_region)
    pdf.image(grafico_3, x=10, y=pdf.get_y() + 10, w=180)
    pdf.ln(80)
    os.remove(grafico_3)
    
    #indices estacionales
    texto_indices, grafico_indices = tendencias_estacionales(df)
    pdf.add_page()
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Índice Estacional y Tendencias", 0, 1)
    pdf.set_font("Arial", "", 10)
    pdf.multi_cell(0, 10, texto_indices)
    pdf.image(grafico_indices, x=10, y=pdf.get_y() + 10, w=180)
    os.remove(grafico_indices)

    pdf.output(nombre_archivo)
    print(f"Informe guardado como {nombre_archivo}")


# Función para el menú interactivo
def menu_interactivo(df, ventas_por_producto, ventas_por_region):
    while True:
        print("\n--- Menú Interactivo ---")
        print("1. Filtrar por Producto")
        print("2. Filtrar por Rango de Fechas")
        print("3. Salir")

        opcion = input("Selecciona una opción (1-3): ")

        if opcion == "1":
            producto = input("Ingresa el nombre del producto: ")
            if producto in ventas_por_producto:
                datos_producto = df[df['producto'] == producto]
                print(f"\n--- Informe para el Producto: {producto} ---")
                print(f"Total Venta: ${ventas_por_producto[producto]:.2f}")
                print(datos_producto[['fecha_venta', 'cantidad', 'total_venta']])
            else:
                print("Producto no encontrado.")

        elif opcion == "2":
            fecha_inicio = input("Ingresa la fecha de inicio (dd/mm/yyyy): ")
            fecha_fin = input("Ingresa la fecha de fin (dd/mm/yyyy): ")
            try:
                fecha_inicio_dt = pd.to_datetime(fecha_inicio, format='%d/%m/%Y')
                fecha_fin_dt = pd.to_datetime(fecha_fin, format='%d/%m/%Y')
                datos_rango = df[(df['fecha_venta'] >= fecha_inicio_dt) & (df['fecha_venta'] <= fecha_fin_dt)]
                
                if not datos_rango.empty:
                    print(f"\n--- Informe de Ventas del {fecha_inicio} al {fecha_fin} ---")
                    print(datos_rango[['fecha_venta', 'producto', 'cantidad', 'total_venta']])
                else:
                    print("No se encontraron ventas en el rango de fechas especificado.")
            except ValueError:
                print("Formato de fecha no válido. Usa dd/mm/yyyy.")

        elif opcion == "3":
            print("Saliendo del menú interactivo.")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")
            
# Menú principal para seleccionar opciones
def menu_principal():
    archivo = 'ventas.csv'
    df = cargar_datos(archivo)
    transacciones, ventas_por_producto, ventas_por_region = estructurar_datos(df)

    while True:
        print("\n--- Menú Principal ---")
        print("1. Estructurar datos en lista(Total transacciones)y diccionarios (Ventas por Producto/Ventas por Región) formato tabla")
        print("2. Calcular Promedios de Ventas (diario y mensual)")
        print("3. Ver Producto Más y Menos Vendido")
        print("4. Ver tendencias estacionales")
        print("5. Grafica distribucion de ventas por producto")
        print("6. Grafica evolucion ventas a lo largo del tiempo")
        print("7. Grafica ventas por producto/ventas por region")
        print("8. Generar Informe en PDF")
        print("9. Menú Interactivo (Primero ejecuta las opciones anteriores para evitar errores)")
        print("10. Salir")
        opcion = input("Selecciona una opción (1-10): ")

        if opcion == "1":
            total_ventas_por_producto_region(transacciones, ventas_por_producto, ventas_por_region)
        
        elif opcion == "2":
            promedio_diario, promedio_mensual = promedio_ventas(df)
        
        elif opcion == "3":
            productos_extremos(ventas_por_producto)
        
        elif opcion == "4":
            tendencias_estacionales_mostrar(df)
            
        elif opcion == "5":
            grafica_distribucion_ventas_mostrar(ventas_por_producto)

        elif opcion == "6":
            grafica_evolucion_ventas_mostrar(df)
            
        elif opcion == "7":
            grafica_comparacion_productos_regiones_mostrar(ventas_por_producto, ventas_por_region)

        elif opcion == "8":
            promedio_diario, promedio_mensual = promedio_ventas(df, imprimir=False)
            max_ventas = max(ventas_por_producto, key=ventas_por_producto.get)
            min_ventas = min(ventas_por_producto, key=ventas_por_producto.get)
            ventas_mensuales = df.groupby(df['fecha_venta'].dt.month)['total_venta'].sum()
            generar_informe_pdf("Informe_Ventas.pdf", ventas_por_producto, ventas_por_region, promedio_diario, promedio_mensual, max_ventas, min_ventas, df)
     
        elif opcion == "9":
            menu_interactivo(df, ventas_por_producto, ventas_por_region)

        elif opcion == "10":
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción inválida. Por favor, selecciona entre 1 y 10.")



# Ejecutar el menú principal
menu_principal()
