import pandas as pd
import difflib

# Cargar los archivos CSV
embalses = pd.read_csv('export.csv')
lista = pd.read_csv('export(1).csv')

# Crear una lista para almacenar los resultados
resultados = []

# Iterar por cada fila de la tabla 'embalses'
for index, row_embalses in embalses.iterrows():
    nombre_embalses = row_embalses['EMBALSE_NOMBRE']
    ambito_nombre = row_embalses['AMBITO_NOMBRE']
    id_embalse = row_embalses['ID']  # Obtener el ID del embalse

    # Realizar fuzzy matching entre 'AMBITO_NOMBRE' y 'DEMARC' en la tabla 'lista'
    demarc_matches = difflib.get_close_matches(ambito_nombre, lista['DEMARC'], n=1, cutoff=0.9)

    if demarc_matches:
        # Filtrar la tabla 'lista' con el resultado del fuzzy matching en 'DEMARC'
        lista_filtrada = lista[lista['DEMARC'] == demarc_matches[0]]

        # Realizar fuzzy matching entre los nombres de embalses en las filas coincidentes
        embalse_matches = difflib.get_close_matches(nombre_embalses, lista_filtrada['NOMBRE'], n=1, cutoff=0.6)

        # Almacenar el nombre original, el ámbito, el ID y el emparejado (si existe)
        if embalse_matches:
            resultados.append({
                'ID_Embalse': id_embalse,  # Añadir ID del embalse
                'Nombre_Embalses': nombre_embalses,
                'Ambito_Nombre': ambito_nombre,
                'Nombre_Emparejado': embalse_matches[0],
                'Demarc_Emparejado': demarc_matches[0]
            })
        else:
            resultados.append({
                'ID_Embalse': id_embalse,  # Añadir ID del embalse
                'Nombre_Embalses': nombre_embalses,
                'Ambito_Nombre': ambito_nombre,
                'Nombre_Emparejado': None,
                'Demarc_Emparejado': demarc_matches[0]
            })
    else:
        resultados.append({
            'ID_Embalse': id_embalse,  # Añadir ID del embalse
            'Nombre_Embalses': nombre_embalses,
            'Ambito_Nombre': ambito_nombre,
            'Nombre_Emparejado': None,
            'Demarc_Emparejado': None
        })

# Convertir los resultados en un DataFrame
resultados_df = pd.DataFrame(resultados)

# Exportar el DataFrame a un nuevo archivo CSV
resultados_df.to_csv('quizas.csv', index=False)

print("Fuzzy matching completado y datos exportados a 'res_FM.csv'.")
