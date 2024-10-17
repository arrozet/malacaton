import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Cargar el archivo CSV
df = pd.read_csv("aguaBien.csv")

# Convertir la columna FECHA a formato datetime especificando el formato correcto
df['FECHA'] = pd.to_datetime(df['FECHA'], format="%d/%m/%y %H:%M")

# Añadir una columna booleana que indica si el agua baja del 25% de la capacidad total
df['BAJO_25_PORCIENTO'] = df['AGUA_ACTUAL'] < (0.25 * df['AGUA_TOTAL'])

# Eliminar filas con valores NaN en AGUA_ACTUAL o AGUA_TOTAL
df = df.dropna(subset=['AGUA_ACTUAL', 'AGUA_TOTAL'])

# Obtener todos los IDs de embalses únicos
embalses_ids = df["ID"].unique()

# Crear un DataFrame para almacenar las predicciones
predicciones_totales = pd.DataFrame()


# Función para convertir las fechas en una representación numérica
def convertir_fecha_a_num(fecha):
    return fecha.toordinal()


# Iterar sobre cada embalse
for embalse_id in embalses_ids:
    # Filtrar por el embalse actual
    df_embalse = df[df["ID"] == embalse_id].sort_values("FECHA")

    # Establecer la fecha como índice
    df_embalse.set_index("FECHA", inplace=True)

    # Si el embalse no tiene suficientes datos, saltarlo
    if len(df_embalse) < 2:
        continue

    # Convertir las fechas en números
    df_embalse['FECHA_NUM'] = df_embalse.index.map(convertir_fecha_a_num)

    # Definir las variables dependientes e independientes
    X = df_embalse[['FECHA_NUM']]
    y = df_embalse['AGUA_ACTUAL']

    # Comprobar si hay NaN en las variables de entrada o salida
    if y.isnull().any() or X.isnull().any().any():
        print(f"El embalse {embalse_id} tiene datos incompletos, se omite.")
        continue

    # Crear el modelo de regresión lineal
    model = LinearRegression()

    # Ajustar el modelo a los datos históricos
    model.fit(X, y)

    # Predecir los próximos 12 meses
    last_date = df_embalse.index[-1]
    future_dates = pd.date_range(last_date, periods=13, freq='MS')[1:]  # Próximos 12 meses

    # Convertir las fechas futuras a formato numérico
    future_dates_num = np.array([convertir_fecha_a_num(fecha) for fecha in future_dates]).reshape(-1, 1)

    # Predecir la cantidad de agua para las fechas futuras
    forecast = model.predict(future_dates_num)

    # Crear un DataFrame con las predicciones para este embalse
    forecast_df = pd.DataFrame({
        'FECHA': future_dates,
        'PREDICCION_AGUA': forecast,
        'ID_EMBALSE': embalse_id,
        'AGUA_TOTAL': df_embalse['AGUA_TOTAL'].iloc[0]  # Suponemos que AGUA_TOTAL no cambia
    })

    # Añadir una columna booleana que indica si el agua predicha baja del 25% de la capacidad total
    forecast_df['BAJO_25_PORCIENTO'] = forecast_df['PREDICCION_AGUA'] < (0.25 * forecast_df['AGUA_TOTAL'])

    # Añadir las predicciones al DataFrame total
    predicciones_totales = pd.concat([predicciones_totales, forecast_df])

# Guardar el nuevo archivo CSV con la columna adicional
predicciones_totales.to_csv('predicciones_embalses_con_bajo_25_por_ciento.csv', index=False)

print("Archivo generado correctamente: predicciones_embalses_con_bajo_25_por_ciento.csv")
