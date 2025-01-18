# Importamos Libreria
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Cargar el dataset
df = pd.read_excel('Book1.xlsx')

# Eliminamos Nulos
dfLim = df.dropna()

# Reiniciamos el indice
dfLim.reset_index(inplace=True,drop=True)

# Escogemos las columnas que vamos a usar
dfLim[['Cat','SKU','Stock','CLASIFICACION']]

# Agrupar los datos por la columna 'Cat' y calcular el total de stock por cat
df_suma = dfLim.groupby('Category').sum()['Stock']

# Mostrar los resultados
print(df_suma.sort_values(ascending=False))