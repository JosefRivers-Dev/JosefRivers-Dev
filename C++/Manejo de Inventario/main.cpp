#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <algorithm>

using namespace std;

// Estructura para representar un pedido
struct Pedido {
    string id;
    string descripcion;
    string idVehiculo; // Agregamos un campo para la identificación del vehículo asignado
};

// Estructura para representar un vehículo
struct Vehiculo {
    string id;
    string descripcion;
    bool disponible;
};

// Estructura para representar un almacen
struct Almacen {
    string id; // ID del almacén
    string descripcion; // Descripcion del almacen
    int cantidad; // Cantidad de productos en el almacen
};

// Vectores para almacenar los pedidos y vehículos
vector<Pedido> pedidos;

// Lista para almacenar los vehículos
list<Vehiculo> vehiculos;

// Vector para almacenar información sobre almacenes
vector<Almacen> almacenes;

// Función para agregar un pedido
void agregarPedido() {
    Pedido nuevoPedido;

    cout << "Ingrese el ID del pedido: ";
    cin >> nuevoPedido.id;
    cin.ignore(); // Para limpiar el buffer de entrada

    cout << "Ingrese la descripción del pedido: ";
    getline(cin, nuevoPedido.descripcion);

    // inicialmente, no hay ningún vehículo asignado al pedido
    nuevoPedido.idVehiculo = "";

    // Agregamos el pedido al vector de pedidos
    pedidos.push_back(nuevoPedido);

    cout << "Pedido agregado exitosamente." << endl;
}

// Función para eliminar un pedido
void eliminarPedido() {
    string idPedido;
    cout << "Ingrese el ID del pedido a eliminar: ";
    cin >> idPedido;

    auto itPedido = find_if(pedidos.begin(), pedidos.end(), [&idPedido](const Pedido& pedido) { return pedido.id == idPedido; });

    if (itPedido != pedidos.end()) {
        pedidos.erase(itPedido);
        cout << "Pedido eliminado exitosamente." << endl;
    } else {
        cout << "No se encontró el pedido con el ID ingresado." << endl;
    }
}

// Función para modificar un pedido
void modificarPedido() {
    string idPedido;
    cout << "Ingrese el ID del pedido a modificar: ";
    cin >> idPedido;

    auto itPedido = find_if(pedidos.begin(), pedidos.end(), [&idPedido](const Pedido& pedido) { return pedido.id == idPedido; });

    if (itPedido != pedidos.end()) {
        cout << "Ingrese la nueva descripción del pedido: ";
        cin.ignore();
        getline(cin, itPedido->descripcion);
        cout << "Pedido modificado exitosamente." << endl;
    } else {
        cout << "No se encontró el pedido con el ID ingresado." << endl;
    }
}

// Función para gestionar un pedido
void gestionarPedido() {
    int opcion;

    do {
        cout << "\nGestión de Pedidos\n";
        cout << "1. Agregar pedido\n";
        cout << "2. Eliminar pedido\n";
        cout << "3. Modificar pedido\n";
        cout << "4. Volver al menú principal\n";
        cout << "Ingrese la opción deseada: ";
        cin >> opcion;

        switch (opcion) {
            case 1:
                agregarPedido();
                break;
            case 2:
                eliminarPedido();
                break;
            case 3:
                modificarPedido();
                break;
            case 4:
                break;
            default:
                cout << "Opción no válida. Por favor, intenta de nuevo.\n";
                break;
        }
    } while (opcion != 4);
}

// Función para eliminar un vehículo
void eliminarVehiculo() {
    string id;
    cout << "Ingrese el ID del vehículo a eliminar: ";
    cin >> id;

    for (auto it = vehiculos.begin(); it != vehiculos.end(); ++it) {
        if (it->id == id) {
            vehiculos.erase(it);
            cout << "Vehículo eliminado exitosamente." << endl;
            return;
        }
    }

    cout << "No se encontró el vehículo con el ID proporcionado." << endl;
}

// Función para agregar un vehículo
void agregarVehiculo() {
    Vehiculo nuevoVehiculo;

    cout << "Ingrese el ID del vehículo: ";
    cin >> nuevoVehiculo.id;
    cin.ignore(); // Para limpiar el buffer de entrada

    cout << "Ingrese la descripción del vehículo: ";
    getline(cin, nuevoVehiculo.descripcion);

    // inicialmente, el vehículo está disponible
    nuevoVehiculo.disponible = true;

    // Agregamos el vehículo a la lista de vehículos
    vehiculos.push_back(nuevoVehiculo);

    cout << "Vehículo agregado exitosamente." << endl;
}

// Función para modificar un vehículo
void modificarVehiculo() {
    string id;
    cout << "Ingrese el ID del vehículo a modificar: ";
    cin >> id;

    for (auto& vehiculo : vehiculos) {
        if (vehiculo.id == id) {
            cout << "Ingrese la nueva descripción del vehículo: ";
            cin.ignore(); // Para limpiar el buffer de entrada
            getline(cin, vehiculo.descripcion);

            cout << "Vehiculo modificado exitosamente." << endl;
            return;
        }
    }

    cout << "No se encontró el vehículo con el ID proporcionado." << endl;
}

// Función para gestionar un vehículo
void gestionarVehiculo() {
    int opcion;

    do {
        cout << "\n1. Agregar vehículo\n2. Eliminar vehículo\n3. Modificar vehículo\n4. Regresar al menú principal\nIngrese una opción: ";
        cin >> opcion;

        switch (opcion) {
            case 1:
                agregarVehiculo();
                break;
            case 2:
                eliminarVehiculo();
                break;
            case 3:
                modificarVehiculo();
                break;
            case 4:
                break;
            default:
                cout << "Opción no valida. Intente de nuevo." << endl;
                break;
        }
    } while (opcion != 4);
}

// Función para asignar un vehículo a un pedido
void asignarVehiculo() {
    string idPedido, idVehiculo;
    cout << "Ingrese el ID del pedido: ";
    cin >> idPedido;
    cout << "Ingrese el ID del vehículo: ";
    cin >> idVehiculo;

    // Buscamos el pedido y el vehículo en los vectores correspondientes
    auto itPedido = find_if(pedidos.begin(), pedidos.end(), [&idPedido](const Pedido& pedido) { return pedido.id == idPedido; });
    auto itVehiculo = find_if(vehiculos.begin(), vehiculos.end(), [&idVehiculo](const Vehiculo& vehiculo) { return vehiculo.id == idVehiculo; });

    // Verificamos que el pedido y el vehículo existen y que el vehículo está disponible
    if (itPedido != pedidos.end() && itVehiculo != vehiculos.end() && itVehiculo->disponible) {
        itPedido->idVehiculo = idVehiculo; // Asignamos el vehículo al pedido
        itVehiculo->disponible = false; // Marcamos el vehículo como no disponible
        cout << "Vehiculo asignado exitosamente al pedido." << endl;
    } else {
        cout << "No se pudo asignar el vehículo al pedido. Verifique los ID ingresados y la disponibilidad del vehículo." << endl;
    }
}

// Función para consultar el estado de un envío
void consultarEstado() {
    string idPedido;
    cout << "Ingrese el ID del pedido: ";
    cin >> idPedido;

    // Buscamos el pedido en el vector de pedidos
    auto itPedido = find_if(pedidos.begin(), pedidos.end(), [&idPedido](const Pedido& pedido) { return pedido.id == idPedido; });

    // Verificamos que el pedido existe
    if (itPedido != pedidos.end()) {
        // Mostramos la información del pedido
        cout << "ID del pedido: " << itPedido->id << endl;
        cout << "Descripcion del pedido: " << itPedido->descripcion << endl;
        cout << "ID del vehículo asignado: " << (itPedido->idVehiculo.empty() ? "Ninguno" : itPedido->idVehiculo) << endl;
    } else {
        cout << "No se encontró el pedido con el ID ingresado." << endl;
    }
}

// Función para planificar una ruta de transporte
void planificarRuta() {
    string idPedido;
    cout << "Ingrese el ID del pedido para el que se planificara la ruta: ";
    cin >> idPedido;

    // Buscamos el pedido en el vector de pedidos
    auto itPedido = find_if(pedidos.begin(), pedidos.end(), [&idPedido](const Pedido& pedido) { return pedido.id == idPedido; });

    // Verificamos que el pedido existe y que tenemos un vehículo asignado
    if (itPedido != pedidos.end() && !itPedido->idVehiculo.empty()) {
        // Aquí iría la lógica para planificar la ruta
        cout << "Ruta planificada exitosamente para el pedido " << idPedido << "." << endl;
    } else {
        cout << "No se pudo planificar la ruta. Verifique que el ID del pedido sea correcto y que tenga un vehículo asignado." << endl;
    }
}

// Función para verificar la disponibilidad de vehículos
void verificarDisponibilidad() {
    // Recorremos el vector de vehículos y mostramos solo los que están disponibles
    for (const auto& vehiculo : vehiculos) {
        if (vehiculo.disponible) {
            cout << "ID del vehículo: " << vehiculo.id << endl;
            cout << "Descripcion del vehiculo: " << vehiculo.descripcion << endl;
        }
    }
}

// Función para actualizar la información de un almacen
void actualizarAlmacen() {
    string idAlmacen;
    int nuevaCantidad;

    cout << "Ingrese el ID del almacen: ";
    cin >> idAlmacen;

    // Buscamos el almacen en el vector de almacenes
    auto itAlmacen = find_if(almacenes.begin(), almacenes.end(), [&idAlmacen](const Almacen& almacen) { return almacen.id == idAlmacen; });

    // Verificamos que el almacen existe
    if (itAlmacen != almacenes.end()) {
        // Solicitamos la nueva cantidad de productos en el almacen
        cout << "Ingrese la nueva cantidad de productos en el almacen: ";
        cin >> nuevaCantidad;

        // Actualizamos la cantidad de productos en el almacen
        itAlmacen->cantidad = nuevaCantidad;

        cout << "Informacion del almacen actualizada exitosamente." << endl;
    } else {
        cout << "No se encontró el almacen con el ID ingresado." << endl;
    }
}

// Función para salir del sistema
void salir() {
    cout << "Saliendo del sistema..." << endl;
    exit(0);
}

int main() {
    int opcion;

    do {
        cout << "\nSistema de Gestión Logística\n";
        cout << "1. Gestionar pedido\n";
        cout << "2. Gestionar vehiculo\n";
        cout << "3. Asignar vehículo a pedido\n";
        cout << "4. Consultar estado de envío\n";
        cout << "5. Planificar ruta de transporte\n";
        cout << "6. Verificar disponibilidad de vehículos\n";
        cout << "7. Actualizar información de almacen\n";
        cout << "8. Salir\n";
        cout << "Ingrese la opción deseada: ";
        cin >> opcion;

        switch (opcion) {
            case 1:
                gestionarPedido();
                break;
            case 2:
                gestionarVehiculo();
                break;
            case 3:
                asignarVehiculo();
                break;
            case 4:
                consultarEstado();
                break;
            case 5:
                planificarRuta();
                break;
            case 6:
                verificarDisponibilidad();
                break;
            case 7:
                actualizarAlmacen();
                break;
            case 8:
                salir();
                break;
            default:
                cout << "Opción no válida. Por favor, intenta de nuevo.\n";
                break;
        }
    } while (opcion != 8);

    return 0;
}