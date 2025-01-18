# Una forma de cargar el archivo solo top 5
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Lee el archivo CSV con una codificación específica
df = pd.read_csv('INE_DISTRITO_2020.csv', encoding='latin1')

# Muestra las primeras filas del DataFrame para verificar que se haya leído correctamente
print(df.head())

# Agrupa por 'NOM_ENT' y cuenta el número de registros en cada grupo
count_by_nom_ent = df.groupby('NOM_ENT ').size().reset_index(name='Count')

# Muestra el resultado
print(count_by_nom_ent)

# Crear la gráfica de barras
# Ver los tamaños el primer dato es el ancho, el segundo es lo largo 
plt.figure(figsize=(10, 5))
plt.bar(count_by_nom_ent['NOM_ENT '], count_by_nom_ent['Count'], color='blue')
plt.xlabel('')
plt.ylabel('Registros')
plt.title('Registros por Entidad')
# Rotar las etiquetas del eje x para que se lean mejor
plt.xticks(rotation=85)
plt.tight_layout()
# Mostrar la gráfica
plt.show()

# Crear la gráfica de barras usando seaborn
plt.figure(figsize=(10, 5))
sns.barplot(x='Count', y='NOM_ENT ', data=count_by_nom_ent, palette='viridis')
plt.xlabel('')
plt.ylabel('Registros')
plt.title('Registros por Entidad')
plt.xticks(rotation=90)
plt.tight_layout()
# Mostrar la gráfica
plt.show()