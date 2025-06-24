# Reporte de Queries

![SAP](https://img.shields.io/badge/SAP-Business%20One-blue) ![SQL](https://img.shields.io/badge/SQL-Queries-green) ![Database](https://img.shields.io/badge/Database-Operations-yellow)

Queries aplicados en el negocio para poder obtimizar algunas formas de trabajo, que con el tiempo ayudo a que se convirtieran en flujos de trabajo, para una mejor distribucion de la informacion para el poryecto o negoció.

## Consultas Disponibles

### 📦 `Costos_Articulos.sql`
- **Propósito**: Obtener el costo promedio de artículos en almacén específico
- **Tablas**: `OITW` (Items por almacén), `OITM` (Maestro de artículos)
- **Filtro**: Almacén 'ALPM' (Mayoreo)
- **Campos**: Código, Nombre y Precio promedio del artículo

### 📍 `Direcion_Orden_Compra.sql`
- **Propósito**: Consultar direcciones de clientes para órdenes de compra
- **Tablas**: `OCRD` (Maestro de negocios), `CRD1` (Direcciones), `OSLP` (Vendedores), `OSHP` (Transportistas)
- **Filtro**: Clientes con código que comienza por 'CM'
- **Campos**: Dirección completa, datos de contacto y logística

### 💰 `Facturacion.sql`
- **Propósito**: Reporte detallado de facturación con análisis de márgenes
- **Tablas**: `OINV` (Facturas), `ORIN` (Notas de crédito), `INV1`/`RIN1` (Líneas)
- **Filtro**: Documentos no cancelados desde junio 2024
- **Campos**: Datos de venta, categorización, impuestos y ganancias

### 📊 `Inventario por Almacen.sql`
- **Propósito**: Reporte de inventario con disponibilidad por ubicación
- **Tablas**: `OITW` (Items por almacén), `OITM` (Maestro de artículos)
- **Campos**: Existencia, comprometido y disponible por almacén
- **Destacado**: Mapeo de códigos de almacén a nombres descriptivos

### 👥 `Lista_Cliente.sql`
- **Propósito**: Listado básico de clientes
- **Tabla**: `OCRD` (Maestro de negocios)
- **Campos**: Código, prefijo y nombre del cliente

## Estructura de Base de Datos

Las consultas utilizan las tablas estándar de SAP Business One:
- `OCRD`: Maestro de negocios (clientes/proveedores)
- `OITM`: Maestro de artículos
- `OITW`: Artículos por almacén
- `OINV/ORIN`: Facturas/Notas de crédito
- `INV1/RIN1`: Líneas de documentos

## Cómo Usar

1. Ejecutar directamente en SAP Business One (Menú → Herramientas → Consultas SQL)
2. Usar con SAP HANA Studio para análisis avanzados
3. Adaptar filtros (fechas, códigos) según necesidades

```sql
-- Ejemplo de modificación de filtro de fecha
WHERE T0.DocDate >= '[NuevaFecha]'
```

## Personalización

Para adaptar las consultas:
1. Cambiar códigos de almacén en `CASE` statements
2. Ajustar rangos de fechas
3. Modificar condiciones de filtrado
4. Agregar/eliminar campos según requerimientos

## Mejoras Previstas

- [ ] Convertir a vistas SQL para reutilización
- [ ] Optimizar consultas complejas
- [ ] Añadir parámetros dinámicos
- [ ] Crear versiones para SAP HANA

## Consideraciones

⚠️ **Importante**:
- Verificar permisos de usuario antes de ejecutar
- Las consultas pueden variar según versión de SAP B1
- Hacer pruebas en ambiente de desarrollo primero
