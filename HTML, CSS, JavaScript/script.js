const form = document.getElementById('login-form');
const usuariosTxt = 'usuarios.txt';
const tareasTxt = 'tareas.txt';

form.addEventListener('submit', (e) => {
  e.preventDefault();

  const login = document.getElementById('login').value;
  const password = document.getElementById('password').value;

  fetch(usuariosTxt)
    .then((response) => response.text())
    .then((data) => {
      const usuarios = data.split('\n').map((linea) => linea.trim());
      
      console.log(usuarios)

      const usuarioValido = usuarios.find((usuario) => {
        const [nombreUsuario, email, passwordUsuario] = usuario.split(',');
        return (nombreUsuario === login || email === login) && passwordUsuario === password;
      });

      if (usuarioValido) {
        mostrarInicio();
      } else {
        alert('Credenciales incorrectas');
      }
    })
    .catch((error) => {
      console.error(error);
    });
});

function mostrarInicio() {

  console.log('mostrarInicio() llamada');

  const tareasContainer = document.getElementById('tareas-container');
  tareasContainer.style.display = 'block';
  const loginContainer = document.getElementById('login-container');
  loginContainer.style.display = 'none';

  fetch(tareasTxt)
    .then((response) => response.text())
    .then((data) => {
      const listaTareas = document.getElementById('lista-tareas');
      listaTareas.innerHTML = '';
      const tareas = data.split('\n').map((linea) => linea.trim());
      tareas.forEach((tarea) => {
        const [nombre, descripcion, estado, comentario] = tarea.split(',');
        const tareaBloque = document.createElement('div');
        tareaBloque.className = 'tarea-bloque';
        tareaBloque.innerHTML = `
          <div class="estado-bloque ${estado === 'realizado' ? 'realizado' : estado === 'pendiente' ? 'pendiente' : 'en-proceso'}"></div>
          <div class="informacion-tarea">
            <h2>${nombre}</h2>
            <p>Estado: ${estado}</p>
          </div>
          <div class="acciones-tarea">
            <button class="boton-editar" onclick="mostrarDetalleTarea('${nombre}')">Editar</button>
          </div>
        `;
        listaTareas.appendChild(tareaBloque);
      });
    })
    .catch((error) => {
      console.error(error);
    });
}

function mostrarDetalleTarea(nombreTarea) {
  const detalleTareaContainer = document.getElementById('detalle-tarea-container');
  detalleTareaContainer.style.display = 'block';
  const tareasContainer = document.getElementById('tareas-container');
  tareasContainer.style.display = 'none';

  fetch(tareasTxt)
    .then((response) => response.text())
    .then((data) => {
      const tareas = data.split('\n').map((linea) => linea.trim());
      const tarea = tareas.find((tarea) => {
        const [nombre, descripcion, estado, comentario] = tarea.split(',');
        return nombre === nombreTarea;
      });
      if (tarea) {
        const [nombre, descripcion, estado, comentario] = tarea.split(',');
        document.getElementById('nombre-tarea').textContent = nombre;
        document.getElementById('descripcion-tarea').textContent = descripcion;
        document.getElementById('estado-tarea').textContent = estado;
        document.getElementById('comentario-tarea').textContent = comentario;
        document.getElementById('estado').value = estado;
        document.getElementById('comentario').value = comentario;
      } else {
        console.error('No se encontró la tarea');
      }
    })
    .catch((error) => {
      console.error(error);
    });
}


document.getElementById('guardar-cambios').addEventListener('click', (e) => {
  e.preventDefault();
  const nombreTarea = document.getElementById('nombre-tarea').textContent;
  const estado = document.getElementById('estado').value;
  const comentario = document.getElementById('comentario').value;
  guardarCambiosTarea(nombreTarea, estado, comentario);
});

function guardarCambiosTarea(nombreTarea, estado, comentario) {
  
  console.log('guardarCambiosTarea() llamada');

  fetch(tareasTxt)
    .then((response) => response.text())
    .then((data) => {
      const tareas = data.split('\n').map((linea) => linea.trim());
      const tarea = tareas.find((tarea) => {
        const [nombre, , ,] = tarea.split(',');
        return nombre === nombreTarea;
      });
      const indiceTarea = tareas.indexOf(tarea);
      const [nombre, descripcion, ,] = tarea.split(',');
      tareas[indiceTarea] = `${nombre},${descripcion},${estado},${comentario}`;
      const nuevoTexto = tareas.join('\n');
      fetch(tareasTxt, {
        method: 'PUT',
        headers: {
          'Content-Type': 'text/plain'
        },
        body: nuevoTexto
      })
      .then((response) => response.text())
      .then((data) => {
        alert('Cambios guardados con éxito');
        // Actualiza la vista con los datos modificados
        document.getElementById('estado-tarea').textContent = estado;
        document.getElementById('comentario-tarea').textContent = comentario;
      })
      .catch((error) => {
        console.error(error);
      });
    })
    .catch((error) => {
      console.error(error);
    });
}

document.getElementById('regresar-a-lista').addEventListener('click', (e) => {
  e.preventDefault();
  const listaTareasContainer = document.getElementById('tareas-container');
  listaTareasContainer.style.display = 'block';
  const detalleTareaContainer = document.getElementById('detalle-tarea-container');
  detalleTareaContainer.style.display = 'none';
  mostrarInicio(); // Llamar a la función mostrarInicio() aquí
});