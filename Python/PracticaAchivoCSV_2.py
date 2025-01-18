# Una forma de cargar el archivo solo top 5
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Lee el archivo CSV con una codificación específica
df = pd.read_csv('INE_DISTRITO_2020.csv', encoding='latin1')

# Muestra las primeras filas del DataFrame para verificar que se haya leído correctamente
print(df.head())

# Generar despues un group by por estado o entidad
grouped_df = df.groupby('INDIGENA')['DISTRITO'].sum().reset_index()

# Muestra el DataFrame resultante
print(grouped_df)

# Crear la gráfica de barras
plt.figure(figsize=(10, 5))
plt.bar(grouped_df['INDIGENA'], grouped_df['DISTRITO'], color='blue')
plt.xlabel('')
plt.ylabel('Distritos')
plt.title('Distritos por Grupo Indígena')
# Rota las etiquetas del eje x para mejorar la legibilidad
plt.xticks(rotation=45)
plt.tight_layout()
# Mostrar la gráfica
plt.show()

# Crear la gráfica de barras usando seaborn
plt.figure(figsize=(10, 5))
sns.barplot(x='DISTRITO', y='INDIGENA', data=grouped_df, palette='viridis')
plt.xlabel('')
plt.ylabel('')
plt.title('Distritos por Grupo Indígena')
# Rota las etiquetas del eje x para mejorar la legibilidad
plt.xticks(rotation=45)
plt.tight_layout()
# Mostrar la gráfica
plt.show()