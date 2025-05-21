# Análisis de Datos Demográficos de México

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Pandas](https://img.shields.io/badge/Pandas-1.3%2B-orange) ![Matplotlib](https://img.shields.io/badge/Matplotlib-3.4%2B-green) ![Seaborn](https://img.shields.io/badge/Seaborn-0.11%2B-red)

Análisis de datos del INE sobre distritos electorales y población indígena en México (2020).

## Scripts Disponibles

### 📊 `AnalisisDatos&Graficos_v1.py`
- **Objetivo**: Análisis de registros por entidad federativa
- **Funcionalidades**:
  - Carga de datos desde archivo CSV
  - Agrupación por entidad federativa (`NOM_ENT`)
  - Visualización con:
    - Gráficas de barras verticales (Matplotlib)
    - Gráficas de barras horizontales (Seaborn)
- **Salidas**:
  - Tabla de conteo por entidad
  - Dos visualizaciones diferentes de los datos

### 📈 `AnalisisDatos&Graficos_v2.py`
- **Objetivo**: Análisis de distritos por población indígena
- **Funcionalidades**:
  - Agrupación por indicador indígena (`INDIGENA`)
  - Suma de distritos por grupo
  - Visualización con:
    - Gráficas de barras verticales (Matplotlib)
    - Gráficas de barras horizontales (Seaborn)
- **Salidas**:
  - Tabla de distritos por grupo indígena
  - Dos visualizaciones de la distribución

## Requisitos
```
bash
pip install pandas matplotlib seaborn
```

## Estructura de Datos Esperada

Los scripts esperan un archivo `INE_DISTRITO_2020.csv` con al menos las columnas:
- `NOM_ENT` (nombre de entidad federativa)
- `INDIGENA` (indicador de población indígena)
- `DISTRITO` (identificador de distrito)

## Ejecución

1. Colocar el archivo CSV en el mismo directorio que los scripts
2. Ejecutar cualquiera de los scripts:

```
bash
python AnalisisDatos&Graficos_v1.py
python AnalisisDatos&Graficos_v2.py
```

## Resultados Esperados

Cada script generará:
1. Output en consola con:
   - Muestra de las primeras filas del dataset
   - Resultados del agrupamiento
2. Ventanas emergentes con:
   - Gráfico de Matplotlib
   - Gráfico de Seaborn

## Personalización

Para adaptar los scripts:
- Modificar `figsize` para cambiar dimensiones de gráficos
- Ajustar `rotation` en `xticks` para mejor legibilidad
- Cambiar `palette` en Seaborn para diferentes esquemas de color
