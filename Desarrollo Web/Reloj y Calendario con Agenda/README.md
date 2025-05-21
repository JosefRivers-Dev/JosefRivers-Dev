# Agenda Digital con Reloj y Calendario Semanal

Una aplicación web minimalista que combina un reloj digital con un calendario semanal para organizar tareas, con un diseño inspirado en terminales de computadora.

## Características principales

- **Reloj digital** en tiempo real con formato 24 horas
- **Fecha actual** mostrada bajo el reloj
- **Calendario semanal** con espacios para tareas diarias
- Función para marcar tareas como completadas
- Diseño futurista con tema oscuro y acentos verdes
- Totalmente responsivo

## Tecnologías utilizadas

- HTML5
- CSS3 (Flexbox)
- JavaScript (manejo del DOM y Date API)

## Cómo usar

1. Abre el archivo `index.html` en tu navegador web
2. Observa el reloj y fecha actual en la parte superior
3. En cada día de la semana:
   - Escribe tus tareas en los campos de texto
   - Marca como completada con el botón ✔️
   - El botón cambiará a ❌ si deseas desmarcar

## Personalización

Puedes modificar los estilos en `style.css`:
- Cambiar colores (variables CSS en la sección `body`)
- Ajustar tamaños de fuente
- Modificar el diseño del calendario

## Requisitos del sistema

- Navegador web moderno (Chrome, Firefox, Edge, Safari)
- Conexión a internet (para cargar la fuente Orbitron si no está instalada localmente)

## Mejoras potenciales

- [ ] Persistencia de tareas usando localStorage
- [ ] Notificaciones para tareas pendientes
- [ ] Opción para agregar múltiples tareas por día
- [ ] Sincronización con calendarios externos (Google Calendar, etc.)
- [ ] Versión móvil optimizada

## Capturas de pantalla

<!-- Puedes incluir imágenes aquí -->

## Licencia

Este proyecto está bajo licencia MIT. Siéntete libre de usarlo y modificarlo según tus necesidades.

---

**Nota:** Para obtener la mejor experiencia visual, se recomienda usar la fuente Orbitron. Si no se visualiza correctamente, puedes instalarla o importarla desde Google Fonts añadiendo este enlace en el `<head>` de tu HTML:

```html
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500&display=swap" rel="stylesheet">
```