import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from fpdf import FPDF
#Yeimy Tatiana Corzo Lizarazo y Daniel Andres Pinzon Jay Proyecto 2 Analitica de datos
#1. Función para cargar y limpiar los datos
def cargar_datos(archivo):
    df = pd.read_csv(archivo, encoding='latin1', sep=';')
    df.columns = df.columns.str.replace(r'[\t"]', '', regex=True).str.strip()
    df['identificacion_maquina'] = df['identificacion_maquina'].str.strip().replace(r'[\t\n\r]', '', regex=True)
    df['identificacion_maquina'] = df['identificacion_maquina'].replace(r'\s+', ' ', regex=True)  
    df['fecha'] = pd.to_datetime(df['fecha'], dayfirst=True, errors='coerce')
    print("Columnas disponibles en el archivo:", df.columns)
    print(df.head()) 
    return df

#2. Función para estructuras datos(listas y diccionarios)
def estructurar_datos_en_listas(df):
    ciclos_produccion = []
    for _, row in df.iterrows():
        ciclo = {
            'identificacion_maquina': row['identificacion_maquina'],
            'tiempo_operacion': row['tiempo_operacion'],
            'tiempo_inactividad': row['tiempo_inactividad'],
            'tipo_error': row['tipo_error'],
            'unidades_producidas': row['unidades_producidas']
        }
        ciclos_produccion.append(ciclo)
    
    ciclos_df = pd.DataFrame(ciclos_produccion)
    
    print("\n--- Datos Estructurados en Formato de Tabla ---")
    print(ciclos_df.to_string()) 
    return ciclos_produccion

def estructurar_datos_por_maquina_turno(df):
    datos_organizados = {}

    for _, row in df.iterrows():
        maquina = row['identificacion_maquina']
        turno = row['turno_trabajo']
        tipo_error = row['tipo_error']
        tiempo_operacion = row['tiempo_operacion']
        tiempo_inactividad = row['tiempo_inactividad']
        
        if maquina not in datos_organizados:
            datos_organizados[maquina] = []

        datos_organizados[maquina].append({
            'Turno': turno,
            'Errores': tipo_error,
            'Tiempo Operación': tiempo_operacion,
            'Tiempo Inactividad': tiempo_inactividad
        })

    return datos_organizados

def limpiar_datos(df):
    print("\n--- Limpieza de datos ---")
    df.dropna(subset=['identificacion_maquina', 'tiempo_operacion', 'unidades_producidas'], inplace=True)
    df['tiempo_operacion'] = pd.to_numeric(df['tiempo_operacion'], errors='coerce').fillna(0)
    df['tiempo_inactividad'] = pd.to_numeric(df['tiempo_inactividad'], errors='coerce').fillna(0)
    df['unidades_producidas'] = pd.to_numeric(df['unidades_producidas'], errors='coerce').fillna(0)
    df.drop_duplicates(inplace=True)
    
    print("Limpieza realizada. Datos consistentes y precisos.")
    print(df.head(10).to_string(index=False))
    return df

#3. Analisis de la eficiencia de produccion
# eficiencia de producción
def analizar_eficiencia(df):
    print("\n--- Análisis de Eficiencia de Producción ---")
    resultados = []
    df_copy = df.copy()

    for maquina, data in df_copy.groupby('identificacion_maquina'):
        tiempo_operacion_total = data['tiempo_operacion'].sum()
        tiempo_inactividad_total = data['tiempo_inactividad'].sum()
        tiempo_total = tiempo_operacion_total + tiempo_inactividad_total

        if tiempo_total > 0:
            eficiencia = tiempo_operacion_total / tiempo_total
        else:
            eficiencia = 0
        if eficiencia < 0.9:
            causa = data['tipo_error'].mode()[0] if not data['tipo_error'].isnull().all() else "Desconocida"
            estado_rendimiento = "Bajo Rendimiento"
        else:
            causa = "N/A"
            estado_rendimiento = "Adecuado"

        resultados.append({
            'Nombre Máquina': maquina,
            'Eficiencia de Producción': eficiencia,
            'Estado': estado_rendimiento,
            'Causa': causa
        })

    df_resultados = pd.DataFrame(resultados)
    print(df_resultados.to_string(index=False))

    eficiencia_texto = df_resultados.to_string(index=False)
    return eficiencia_texto


#tiempos de inactividad y tipos de errores
def evaluar_tiempos_inactividad(df):
    salida = "\n--- Evaluación de Tiempos de Inactividad ---\n"
    inactividad_resultados = []
    errores_frecuencia_global = {}

    for maquina, data in df.groupby('identificacion_maquina'):
        tiempo_inactividad_total = data['tiempo_inactividad'].sum()
        unidades_producidas_total = data['unidades_producidas'].sum()
        
        errores_frecuencia = data['tipo_error'].value_counts().to_dict()
        for error, frecuencia in errores_frecuencia.items():
            errores_frecuencia_global[error] = errores_frecuencia_global.get(error, 0) + frecuencia

        inactividad_resultados.append({
            'Nombre Máquina': maquina,
            'Tiempo de Inactividad Total': tiempo_inactividad_total,
            'Unidades Producidas Total': unidades_producidas_total,
            'Errores Frecuencia': errores_frecuencia
        })

    df_inactividad = pd.DataFrame(inactividad_resultados)
    salida += df_inactividad.to_string(index=False)
    error_mas_frecuente = max(errores_frecuencia_global, key=errores_frecuencia_global.get)
    salida += f"\nError más frecuente: {error_mas_frecuente}"

    print(salida)
    return salida  

    
#rendimiento por turno.
def analizar_rendimiento_por_turno(df):
    salida = "\n--- Análisis de Rendimiento por Turno de Trabajo ---\n"
    resultados = []

    for maquina, data_maquina in df.groupby('identificacion_maquina'):
        tiempo_operacion_turno = {'Mañana': 0, 'Tarde': 0, 'Noche': 0}
        unidades_producidas_turno = {'Mañana': 0, 'Tarde': 0, 'Noche': 0}
        tasa_productividad_turno = {'Mañana': 0, 'Tarde': 0, 'Noche': 0}
        
        for turno, data_turno in data_maquina.groupby('turno_trabajo'):
            tiempo_operacion = data_turno['tiempo_operacion'].sum()
            unidades_producidas = data_turno['unidades_producidas'].sum()
            tasa_productividad = unidades_producidas / tiempo_operacion if tiempo_operacion > 0 else 0
            
            tiempo_operacion_turno[turno] = tiempo_operacion
            unidades_producidas_turno[turno] = unidades_producidas
            tasa_productividad_turno[turno] = tasa_productividad
        
        resultados.append({
            'Nombre Máquina': maquina,
            'Tiempo Operación Mañana': tiempo_operacion_turno['Mañana'],
            'Unidades Producidas Mañana': unidades_producidas_turno['Mañana'],
            'Tasa Productividad Mañana': round(tasa_productividad_turno['Mañana'], 2),
            'Tiempo Operación Tarde': tiempo_operacion_turno['Tarde'],
            'Unidades Producidas Tarde': unidades_producidas_turno['Tarde'],
            'Tasa Productividad Tarde': round(tasa_productividad_turno['Tarde'], 2),
            'Tiempo Operación Noche': tiempo_operacion_turno['Noche'],
            'Unidades Producidas Noche': unidades_producidas_turno['Noche'],
            'Tasa Productividad Noche': round(tasa_productividad_turno['Noche'], 2)
        })

    df_resultados = pd.DataFrame(resultados)
    salida += df_resultados.replace(0, "N/A").to_string(index=False)
    print(salida)
    return salida

    
#tendencias y patrones estacionales
def analizar_tendencias(df):
    salida = "\n--- Análisis de Tendencias de Rendimiento ---\n"
    df['rendimiento'] = df['tiempo_operacion'] / (df['tiempo_operacion'] + df['tiempo_inactividad'])
    rendimiento_promedio = df['rendimiento'].mean()

    condiciones = [
        (df['rendimiento'] > rendimiento_promedio * 1.1),  
        (df['rendimiento'] < rendimiento_promedio * 0.9)
    ]
    
    opciones = ['Alto rendimiento', 'Bajo rendimiento']
    df['Tendencia de Rendimiento'] = np.select(condiciones, opciones, default='Estable')

    resultado = df[['identificacion_maquina', 'rendimiento', 'Tendencia de Rendimiento']]
    salida += resultado.to_string(index=False)
    print(salida)
    return salida




#4. Graficas
#Unidades producidas y tiempos de inactividad por máquina
def graficar_unidades_inactividad(df):
    print("\n--- Gráficas de Unidades Producidas y Tiempos de Inactividad ---")
    
    produccion_por_maquina = df.groupby('identificacion_maquina')['unidades_producidas'].sum()
    inactividad_por_maquina = df.groupby('identificacion_maquina')['tiempo_inactividad'].sum()
    
    plt.figure(figsize=(10, 6))
    produccion_por_maquina.plot(kind='bar')
    plt.title('Unidades Producidas por Máquina')
    plt.xlabel('Máquina')
    plt.ylabel('Unidades Producidas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 6))
    inactividad_por_maquina.plot(kind='bar', color='orange')
    plt.title('Tiempo de Inactividad por Máquina')
    plt.xlabel('Máquina')
    plt.ylabel('Tiempo de Inactividad')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
#Graficar la evolución del rendimiento de las máquinas 
def graficar_evolucion_rendimiento(df):
    print("\n--- Gráficas de Evolución del Rendimiento de las Máquinas ---")
    df_temp = df.copy()

    if 'fecha' not in df_temp.columns:
        print("La columna 'fecha' es necesaria para crear la gráfica de evolución.")
        return

    df_temp['fecha'] = pd.to_datetime(df_temp['fecha'], errors='coerce')
    df_temp.dropna(subset=['fecha'], inplace=True)

    categorias = {
        "Robots Soldadores": "Robot Soldador",
        "Tornos": "Torno",
        "Prensas Hidráulicas": "Prensa Hidráulica"
    }

    for categoria, nombre_maquina in categorias.items():
        data_categoria = df_temp[df_temp['identificacion_maquina'].str.contains(nombre_maquina)]
        if data_categoria.empty:
            print(f"No se encontraron datos para {categoria}.")
            continue

        plt.figure(figsize=(12, 6))
        
        for maquina, data in data_categoria.groupby('identificacion_maquina'):
            data = data.set_index('fecha').sort_index()
            tiempo_total = data['tiempo_operacion'] + data['tiempo_inactividad']
            eficiencia = data['tiempo_operacion'] / tiempo_total
            plt.plot(data.index, eficiencia, label=f"{maquina} - Eficiencia", marker='o')
        
        plt.title(f"Evolución de la Eficiencia - {categoria}")
        plt.xlabel("Fecha")
        plt.ylabel("Eficiencia")
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.show()

        plt.figure(figsize=(12, 6))
        
        for maquina, data in data_categoria.groupby('identificacion_maquina'):
            data = data.set_index('fecha').sort_index()
            plt.plot(data.index, data['unidades_producidas'], label=f"{maquina} - Producción", marker='o')
        
        plt.title(f"Evolución de la Producción - {categoria}")
        plt.xlabel("Fecha")
        plt.ylabel("Unidades Producidas")
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.show()


# gráficas de pastel de distribución de tipos de errores
def graficar_distribucion_errores(df):
    print("\n--- Gráficas de Distribución de Tipos de Errores ---")
    if 'tipo_error' not in df.columns:
        print("La columna 'tipo_error' es necesaria para crear la gráfica de pastel.")
        return

    categorias = {
        "Robots Soldadores": "Robot Soldador",
        "Tornos": "Torno",
        "Prensas Hidráulicas": "Prensa Hidráulica"
    }

    for categoria, nombre_maquina in categorias.items():
        data_categoria = df[df['identificacion_maquina'].str.contains(nombre_maquina)]
        error_counts = data_categoria['tipo_error'].value_counts()
        
        if error_counts.empty:
            print(f"No se encontraron datos de errores para {categoria}.")
            continue
    
        plt.figure(figsize=(8, 8))
        plt.pie(error_counts, labels=error_counts.index, autopct='%1.1f%%', startangle=140)
        plt.title(f"Distribución de Tipos de Errores - {categoria}")
        plt.tight_layout()
        plt.show()
        
#diagramas de dispersión entre tiempo de inactividad y unidades producidas
def graficar_dispersión_inactividad_produccion(df):
    print("\n--- Diagramas de Dispersión de Tiempo de Inactividad vs Unidades Producidas ---")

    if 'tiempo_inactividad' not in df.columns or 'unidades_producidas' not in df.columns:
        print("Las columnas 'tiempo_inactividad' y 'unidades_producidas' son necesarias para el diagrama de dispersión.")
        return

    categorias = {
        "Robots Soldadores": "Robot Soldador",
        "Tornos": "Torno",
        "Prensas Hidráulicas": "Prensa Hidráulica"
    }

    for categoria, nombre_maquina in categorias.items():
        data_categoria = df[df['identificacion_maquina'].str.contains(nombre_maquina)]
        
        if data_categoria.empty:
            print(f"No se encontraron datos de inactividad y producción para {categoria}.")
            continue

        plt.figure(figsize=(10, 6))
        plt.scatter(data_categoria['tiempo_inactividad'], data_categoria['unidades_producidas'], alpha=0.7)
        plt.title(f"Dispersión de Tiempo de Inactividad vs Unidades Producidas - {categoria}")
        plt.xlabel("Tiempo de Inactividad")
        plt.ylabel("Unidades Producidas")
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        
#5. Optimizacion y mejoras de procesos
#Mejoras
def proponer_mejoras(df):
    mejoras = []

    umbral_inactividad = 40  #Consideramos una alta ineficiencia apartir de las 40 horas de inactividad.

    for _, row in df.iterrows():
        maquina = row['identificacion_maquina']
        tiempo_inactividad = row['tiempo_inactividad']
        tipo_error = row['tipo_error']
        
        if tiempo_inactividad > umbral_inactividad:
            mejora = {
                'maquina': maquina,
                'problema': 'Tiempo de inactividad alto',
                'mejora_propuesta': 'Implementar mantenimiento preventivo'
            }
            mejoras.append(mejora)
        
        if tipo_error == 'Error en soldadura':
            mejora = {
                'maquina': maquina,
                'problema': tipo_error,
                'mejora_propuesta': 'Revisar alineación y calidad de materiales en soldadura'
            }
            mejoras.append(mejora)
        
        elif tipo_error == 'Desgaste de herramienta':
            mejora = {
                'maquina': maquina,
                'problema': tipo_error,
                'mejora_propuesta': 'Reemplazo y monitoreo frecuente de herramientas'
            }
            mejoras.append(mejora)
        
        elif tipo_error == 'Sobrecarga del motor':
            mejora = {
                'maquina': maquina,
                'problema': tipo_error,
                'mejora_propuesta': 'Revisar carga y ajustar velocidad de operación'
            }
            mejoras.append(mejora)
        
        elif tipo_error == 'Fallo en pieza de repuesto':
            mejora = {
                'maquina': maquina,
                'problema': tipo_error,
                'mejora_propuesta': 'Asegurar la calidad y disponibilidad de piezas de repuesto'
            }
            mejoras.append(mejora)

    mejoras_df = pd.DataFrame(mejoras)
    
    print("\n--- Tabla de Mejoras Propuestas ---")
    print(mejoras_df.to_string(index=False))

    return mejoras_df

#Cuello de botella
def identificar_cuellos_de_botella(df):
    cuellos_de_botella = []
    umbral_inactividad = 40  
    umbral_frecuencia_errores = 2  

    
    frecuencia_errores = df['tipo_error'].value_counts().to_dict()

    for _, row in df.iterrows():
        maquina = row['identificacion_maquina']
        tiempo_inactividad = row['tiempo_inactividad']
        tipo_error = row['tipo_error']

        
        if tiempo_inactividad > umbral_inactividad:
            cuello = {
                'maquina': maquina,
                'causa': 'Tiempo de inactividad alto',
                'recomendacion': 'Considerar reprogramación o mantenimiento preventivo adicional'
            }
            cuellos_de_botella.append(cuello)

        
        if frecuencia_errores.get(tipo_error, 0) >= umbral_frecuencia_errores:
            cuello = {
                'maquina': maquina,
                'causa': f'Error frecuente: {tipo_error}',
                'recomendacion': 'Revisión y ajuste del proceso para reducir fallos recurrentes'
            }
            cuellos_de_botella.append(cuello)

    cuellos_df = pd.DataFrame(cuellos_de_botella)
    print("\n--- Cuellos de Botella Identificados ---")
    print(cuellos_df.to_string(index=False))

    return cuellos_df
#Ahorro de costos
def estimar_ahorro_costos(df):
    # Como no contamos con costos. vamos a suponer que el costo por minuto de actividad es de 5 pesos y el costo por unidad producida es de 2 pesos.
    costo_por_minuto_inactividad = 5 
    costo_por_unidad_producida = 2  

    # Aqui tambien asumimos un porcentaje de reuccion de inactividad mediante mejoras en este caso del 20%.
    porcentaje_reduccion_inactividad = 0.20  

    estimaciones = []

    for _, row in df.iterrows():
        maquina = row['identificacion_maquina']
        tiempo_inactividad = row['tiempo_inactividad']
        unidades_producidas = row['unidades_producidas']

        tiempo_reducido = tiempo_inactividad * porcentaje_reduccion_inactividad
        ahorro_coste_inactividad = tiempo_reducido * costo_por_minuto_inactividad

        coste_produccion_actual = unidades_producidas * costo_por_unidad_producida
        estimacion = {
            'maquina': maquina,
            'tiempo_ahorrado': round(tiempo_reducido, 2),  
            'ahorro_coste_inactividad': round(ahorro_coste_inactividad, 2), 
            'coste_produccion_actual': round(coste_produccion_actual, 2)  
        }
        estimaciones.append(estimacion)


    estimaciones_df = pd.DataFrame(estimaciones)
    print("\n--- Estimaciones de Ahorro en Tiempo y Costes ---")
    print(estimaciones_df.to_string(index=False))

    return estimaciones_df

#menu interactivo (hecho con tkinder)
def mostrar_menu_interactivo(df):
    root = tk.Tk()
    root.title("Análisis de Rendimiento")
    root.geometry("400x250")  

    maquina_var = tk.StringVar()
    turno_var = tk.StringVar()
    fecha_inicio_var = tk.StringVar()
    fecha_fin_var = tk.StringVar()
    resultado_text = tk.StringVar()
    maquinas_unicas = sorted(df['identificacion_maquina'].unique())  

    def analizar_rendimiento_personalizado():
        try:
            maquina = maquina_var.get()
            turno = turno_var.get()
            fecha_inicio = datetime.strptime(fecha_inicio_var.get(), '%Y-%m-%d')
            fecha_fin = datetime.strptime(fecha_fin_var.get(), '%Y-%m-%d')
            
            if not maquina or not turno or not fecha_inicio or not fecha_fin:
                resultado_text.set("Por favor, rellena todos los campos.")
                return
        
            df_filtrado = df[(df['identificacion_maquina'] == maquina) & (df['turno_trabajo'] == turno)]
            df_filtrado = df_filtrado[(df_filtrado['fecha'] >= fecha_inicio) & (df_filtrado['fecha'] <= fecha_fin)]
            
            if df_filtrado.empty:
                resultado_text.set("No se encontraron datos para los filtros seleccionados.")
            else:
                unidades_totales = df_filtrado['unidades_producidas'].sum()
                resultado_text.set(f"Análisis de {maquina} en turno {turno}: {unidades_totales} unidades producidas.")
        except ValueError:
            resultado_text.set("Formato de fecha incorrecto. Usa YYYY-MM-DD.")
        except Exception as e:
            resultado_text.set(f"Error en el análisis: {str(e)}")

    ttk.Label(root, text="Máquina:").grid(column=0, row=0, padx=5, pady=5)
    maquina_combo = ttk.Combobox(root, textvariable=maquina_var, values=maquinas_unicas, width=30)
    maquina_combo.grid(column=1, row=0, padx=5, pady=5)
    ttk.Label(root, text="Turno:").grid(column=0, row=1, padx=5, pady=5)
    turno_combo = ttk.Combobox(root, textvariable=turno_var, values=['Mañana', 'Tarde', 'Noche'], width=10)
    turno_combo.grid(column=1, row=1, padx=5, pady=5)
    ttk.Label(root, text="Fecha Inicio (YYYY-MM-DD):").grid(column=0, row=2, padx=5, pady=5)
    fecha_inicio_entry = ttk.Entry(root, textvariable=fecha_inicio_var, width=15)
    fecha_inicio_entry.grid(column=1, row=2, padx=5, pady=5)
    ttk.Label(root, text="Fecha Fin (YYYY-MM-DD):").grid(column=0, row=3, padx=5, pady=5)
    fecha_fin_entry = ttk.Entry(root, textvariable=fecha_fin_var, width=15)
    fecha_fin_entry.grid(column=1, row=3, padx=5, pady=5)
    analizar_button = ttk.Button(root, text="Analizar Rendimiento", command=analizar_rendimiento_personalizado)
    analizar_button.grid(column=0, row=4, columnspan=2, padx=5, pady=10)
    resultado_label = ttk.Label(root, textvariable=resultado_text, wraplength=300)  
    resultado_label.grid(column=0, row=5, columnspan=2, padx=5, pady=5)
    root.mainloop()

#GENERAR INFORME EN UN PDF
#graficas para insertar en el pdf. Lo hemos hecho asi ya que si usabamos una sola funcion (la que definimos anteriormente en el punto 4) teniamos muchisimas fallas de compatibilidad
def guardar_grafico_unidades_inactividad(df):
    produccion_por_maquina = df.groupby('identificacion_maquina')['unidades_producidas'].sum()
    inactividad_por_maquina = df.groupby('identificacion_maquina')['tiempo_inactividad'].sum()
    
    filename_produccion = "grafico_unidades_producidas.png"
    plt.figure(figsize=(10, 6))
    produccion_por_maquina.plot(kind='bar')
    plt.title('Unidades Producidas por Máquina')
    plt.xlabel('Máquina')
    plt.ylabel('Unidades Producidas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(filename_produccion)
    plt.close()

    filename_inactividad = "grafico_inactividad.png"
    plt.figure(figsize=(10, 6))
    inactividad_por_maquina.plot(kind='bar', color='orange')
    plt.title('Tiempo de Inactividad por Máquina')
    plt.xlabel('Máquina')
    plt.ylabel('Tiempo de Inactividad')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(filename_inactividad)
    plt.close()

    return filename_produccion, filename_inactividad

def guardar_grafico_evolucion_rendimiento(df):
    imagenes_generadas = []
    df_temp = df.copy()

    if 'fecha' not in df_temp.columns:
        print("La columna 'fecha' es necesaria para crear la gráfica de evolución.")
        return imagenes_generadas

    df_temp['fecha'] = pd.to_datetime(df_temp['fecha'], errors='coerce')
    df_temp.dropna(subset=['fecha'], inplace=True)

    categorias = {
        "Robots Soldadores": "Robot Soldador",
        "Tornos": "Torno",
        "Prensas Hidráulicas": "Prensa Hidráulica"
    }

    for categoria, nombre_maquina in categorias.items():
        data_categoria = df_temp[df_temp['identificacion_maquina'].str.contains(nombre_maquina)]
        if data_categoria.empty:
            print(f"No se encontraron datos para {categoria}.")
            continue

        filename_eficiencia = f"grafico_eficiencia_{categoria.replace(' ', '_')}.png"
        plt.figure(figsize=(12, 6))
        
        for maquina, data in data_categoria.groupby('identificacion_maquina'):
            data = data.set_index('fecha').sort_index()
            tiempo_total = data['tiempo_operacion'] + data['tiempo_inactividad']
            eficiencia = data['tiempo_operacion'] / tiempo_total
            plt.plot(data.index, eficiencia, label=f"{maquina} - Eficiencia", marker='o')
        
        plt.title(f"Evolución de la Eficiencia - {categoria}")
        plt.xlabel("Fecha")
        plt.ylabel("Eficiencia")
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.savefig(filename_eficiencia)
        plt.close()
        imagenes_generadas.append(filename_eficiencia)

        filename_produccion = f"grafico_produccion_{categoria.replace(' ', '_')}.png"
        plt.figure(figsize=(12, 6))
        
        for maquina, data in data_categoria.groupby('identificacion_maquina'):
            data = data.set_index('fecha').sort_index()
            plt.plot(data.index, data['unidades_producidas'], label=f"{maquina} - Producción", marker='o')
        
        plt.title(f"Evolución de la Producción - {categoria}")
        plt.xlabel("Fecha")
        plt.ylabel("Unidades Producidas")
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.savefig(filename_produccion)
        plt.close()
        imagenes_generadas.append(filename_produccion)

    return imagenes_generadas

def guardar_grafico_distribucion_errores(df):
    imagenes_generadas = []
    
    if 'tipo_error' not in df.columns:
        print("La columna 'tipo_error' es necesaria para crear la gráfica de pastel.")
        return imagenes_generadas

    categorias = {
        "Robots Soldadores": "Robot Soldador",
        "Tornos": "Torno",
        "Prensas Hidráulicas": "Prensa Hidráulica"
    }

    for categoria, nombre_maquina in categorias.items():
        data_categoria = df[df['identificacion_maquina'].str.contains(nombre_maquina)]
        error_counts = data_categoria['tipo_error'].value_counts()
        
        if error_counts.empty:
            print(f"No se encontraron datos de errores para {categoria}.")
            continue

        filename_error = f"grafico_errores_{categoria.replace(' ', '_')}.png"
        plt.figure(figsize=(8, 8))
        plt.pie(error_counts, labels=error_counts.index, autopct='%1.1f%%', startangle=140)
        plt.title(f"Distribución de Tipos de Errores - {categoria}")
        plt.tight_layout()
        plt.savefig(filename_error)
        plt.close()
        
        imagenes_generadas.append(filename_error)

    return imagenes_generadas

def guardar_grafico_dispersion_inactividad_produccion(df):
    imagenes_generadas = []
    
    if 'tiempo_inactividad' not in df.columns or 'unidades_producidas' not in df.columns:
        print("Las columnas 'tiempo_inactividad' y 'unidades_producidas' son necesarias para el diagrama de dispersión.")
        return imagenes_generadas

    categorias = {
        "Robots Soldadores": "Robot Soldador",
        "Tornos": "Torno",
        "Prensas Hidráulicas": "Prensa Hidráulica"
    }

    for categoria, nombre_maquina in categorias.items():
        data_categoria = df[df['identificacion_maquina'].str.contains(nombre_maquina)]
        
        if data_categoria.empty:
            print(f"No se encontraron datos de inactividad y producción para {categoria}.")
            continue

        filename_dispersion = f"grafico_dispersion_{categoria.replace(' ', '_')}.png"
        plt.figure(figsize=(10, 6))
        plt.scatter(data_categoria['tiempo_inactividad'], data_categoria['unidades_producidas'], alpha=0.7)
        plt.title(f"Dispersión de Tiempo de Inactividad vs Unidades Producidas - {categoria}")
        plt.xlabel("Tiempo de Inactividad")
        plt.ylabel("Unidades Producidas")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(filename_dispersion)
        plt.close()
        imagenes_generadas.append(filename_dispersion)

    return imagenes_generadas


# Función para generar el PDF con contenido y gráficos
def generar_pdf(contenido, imagenes=[]):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    max_width = 180  

    for linea in contenido.split("\n"):
        pdf.multi_cell(max_width, 10, txt=linea)
        pdf.ln(5)

    for imagen in imagenes:
        pdf.image(imagen, x=10, w=180)  
        pdf.ln(10)  

    pdf.output("Informe_Rendimiento.pdf")




# Menú principal
def menu_principal():
    archivo = 'Maquinas.csv'
    df = None

    while True:
        print("\n--- Menú Principal ---")
        print("1. Cargar Datos del CSV")
        
        print("--- Estructuracion de datos ---")
        print("2. Estructurar datos en listas y diccionarios")
        print("3. Realizar limpieza de datos")
        
        print("--- Analisis eficiencia de produccion ---")
        print("4. Análisis de la Eficiencia de Producción")
        print("5. Evaluar los tiempos de inactividad")
        print("6. Análisis de rendimiento por turno de trabajo")
        print("7. Análisis de tendencias y patrones estacionales")
        
        print("--- Visualizacion de datos ---")
        print("8. Graficar unidades producidas y tiempos de inactividad")
        print("9. Grafica lineas")
        print("10. Grafica barras")
        print("11. Crear diagramas de dispersión de tiempo de inactividad vs unidades producidas")
        
        print("--- Optimizacion y mejoras del proceso ---")
        print("12. Proponer mejoras de optimización")
        print("13. Identificar cuellos de botella")
        print("14. Estimar ahorro de tiempo y costes")
        
        print("--- Interactividad y procesos ---")
        print("15. Menu interactivo (tkinder)")
        print("16. Generar informe (puede demorar unos cuantos segundos)")
        
        print("17. Salir")
        opcion = input("Selecciona una opción (1-17): ")
        

        if opcion == "1":
            df = cargar_datos(archivo)
            if df is not None:
                print("\n--- Datos del archivo ---")
                print(df.head(10).to_string(index=False)) 
            else:
                print("Error al cargar los datos.")

        elif opcion == "2" and df is not None:
             ciclos_produccion = estructurar_datos_en_listas(df)
             datos_organizados = estructurar_datos_por_maquina_turno(df)
             print("\n--- Diccionarios---")
             pprint(datos_organizados)
             
        elif opcion == "3":
            df = limpiar_datos(df)

        elif opcion == "4" and df is not None:
            analizar_eficiencia(df)
            
        elif opcion == "5" and df is not None:
            evaluar_tiempos_inactividad(df)

        elif opcion == "6" and df is not None:
            analizar_rendimiento_por_turno(df)

        elif opcion == "7" and df is not None:
            analizar_tendencias(df)

        elif opcion == "8" and df is not None:
            graficar_unidades_inactividad(df)
            
        elif opcion == "9" and df is not None:
            graficar_evolucion_rendimiento(df)
            
        elif opcion == "10" and df is not None:
            graficar_distribucion_errores(df)

        elif opcion == "11" and df is not None:
            graficar_dispersión_inactividad_produccion(df)

        elif opcion == "12" and df is not None:
            proponer_mejoras(df)

        elif opcion == "13" and df is not None:
            identificar_cuellos_de_botella(df)

        elif opcion == "14" and df is not None:
            estimar_ahorro_costos(df)

        elif opcion == "15" and df is not None:
            mostrar_menu_interactivo(df)

        elif opcion == "16" and df is not None:
                contenido = ""
                contenido += "Análisis de Eficiencia:\n" + analizar_eficiencia(df) + "\n\n"
                contenido += "Evaluación de Tiempos de Inactividad:\n" + evaluar_tiempos_inactividad(df) + "\n\n"
                contenido += "Análisis de Rendimiento por Turno:\n" + analizar_rendimiento_por_turno(df) + "\n\n"
                contenido += "Análisis de Tendencias y Patrones Estacionales:\n" + analizar_tendencias(df) + "\n\n"
                contenido += "Mejoras Propuestas:\n" + proponer_mejoras(df).to_string(index=False) + "\n\n"
                contenido += "Cuellos de Botella Identificados:\n" + identificar_cuellos_de_botella(df).to_string(index=False) + "\n\n"
                contenido += "Estimaciones de Ahorro en Tiempo y Costos:\n" + estimar_ahorro_costos(df).to_string(index=False) + "\n\n"
                grafico_produccion, grafico_inactividad = guardar_grafico_unidades_inactividad(df)
                graficos_evolucion = guardar_grafico_evolucion_rendimiento(df)
                graficos_errores = guardar_grafico_distribucion_errores(df)
                graficos_dispersion = guardar_grafico_dispersion_inactividad_produccion(df)
                imagenes_para_pdf = [grafico_produccion, grafico_inactividad] + graficos_evolucion + graficos_errores + graficos_dispersion
                generar_pdf(contenido, imagenes=imagenes_para_pdf)
                print("CONTENIDO GUARDADO EN PDF CORRECTAMENTE.")

        elif opcion == "17":
            print("Saliendo del programa.")
            break     

        else:
            print("Opción inválida o datos no cargados. Por favor, selecciona entre 1 y 17.")

# Ejecutar el menú principal
menu_principal()

