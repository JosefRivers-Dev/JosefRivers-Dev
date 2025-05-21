# Sistema de Gestión Logística

Este proyecto es un sistema de gestión logística desarrollado en C++ que permite administrar pedidos, vehículos y almacenes para optimizar el transporte y distribución de mercancías.

## Características principales

- Gestión de pedidos (agregar, eliminar, modificar)
- Gestión de vehículos (agregar, eliminar, modificar)
- Asignación de vehículos a pedidos
- Consulta del estado de envíos
- Planificación de rutas de transporte
- Verificación de disponibilidad de vehículos
- Actualización de información de almacenes

## Estructuras de datos

El programa utiliza las siguientes estructuras principales:

### Pedido (`struct Pedido`)
- `id`: Identificador único del pedido
- `descripcion`: Descripción del contenido del pedido
- `idVehiculo`: ID del vehículo asignado (vacío si no está asignado)

### Vehículo (`struct Vehiculo`)
- `id`: Identificador único del vehículo
- `descripcion`: Descripción del vehículo
- `disponible`: Estado de disponibilidad (true/false)

### Almacén (`struct Almacen`)
- `id`: Identificador único del almacén
- `descripcion`: Descripción del almacén
- `cantidad`: Cantidad de productos en el almacén

## Funcionalidades

1. **Gestión de Pedidos**
   - Agregar nuevos pedidos
   - Eliminar pedidos existentes
   - Modificar información de pedidos

2. **Gestión de Vehículos**
   - Agregar nuevos vehículos
   - Eliminar vehículos existentes
   - Modificar información de vehículos

3. **Operaciones Logísticas**
   - Asignar vehículos a pedidos
   - Consultar estado de envíos
   - Planificar rutas de transporte
   - Verificar disponibilidad de vehículos
   - Actualizar información de almacenes

## Requisitos del sistema

- Compilador de C++ compatible con C++11 o superior
- Sistema operativo Windows, Linux o macOS

## Compilación y ejecución

1. Compilar el programa:
   ```bash
   g++ -std=c++11 gestion_logistica.cpp -o gestion_logistica
   ```

2. Ejecutar el programa:
   ```bash
   ./gestion_logistica
   ```

## Uso

El programa presenta un menú interactivo con las siguientes opciones:

1. Gestionar pedido
2. Gestionar vehículo
3. Asignar vehículo a pedido
4. Consultar estado de envío
5. Planificar ruta de transporte
6. Verificar disponibilidad de vehículos
7. Actualizar información de almacén
8. Salir

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request con tus sugerencias o mejoras.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.