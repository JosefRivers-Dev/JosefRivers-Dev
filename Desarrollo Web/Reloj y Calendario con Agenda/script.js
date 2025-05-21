// Función para actualizar el reloj
function actualizarReloj() {
    const ahora = new Date();
    const horas = ahora.getHours().toString().padStart(2, '0');
    const minutos = ahora.getMinutes().toString().padStart(2, '0');
    const segundos = ahora.getSeconds().toString().padStart(2, '0');
    const dia = ahora.getDate().toString().padStart(2, '0');
    const mes = (ahora.getMonth() + 1).toString().padStart(2, '0');
    const año = ahora.getFullYear();

    const horaActual = `${horas}:${minutos}:${segundos}`;
    const fechaActual = `${dia}/${mes}/${año}`;

    document.getElementById('hora').textContent = horaActual;
    document.getElementById('fecha').textContent = fechaActual;
}

// Actualizar el reloj cada segundo
setInterval(actualizarReloj, 1000);
actualizarReloj(); // Llamada inicial para evitar el retraso de 1 segundo

// Función para marcar tareas como completadas
document.querySelectorAll('.completada').forEach(button => {
    button.addEventListener('click', () => {
        const tarea = button.previousElementSibling;
        tarea.style.textDecoration = tarea.style.textDecoration === 'line-through' ? 'none' : 'line-through';
        button.textContent = tarea.style.textDecoration === 'line-through' ? '✔️' : '❌';
    });
});