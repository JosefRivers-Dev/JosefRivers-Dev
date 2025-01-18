// ---------------------------- Proyecto: Optimizacion del Proceso de Renovación de Licencia ----------------------------
// --------------------------------------- Alumno: Rivera Reyes Jovanny Josef -------------------------------------------
// ------------------------------ Licenciatura en Tecnologia de Informacion y Comunicacion ------------------------------
// ---------------------------------------- Universidad Rosario Castellanos ---------------------------------------------
// --------------------------------------- Materia: Logica de Programacion ----------------------------------------------
// ----------------------------------- Docente: Cosme Antonio Fragado Farias --------------------------------------------
// --------------------------------------- Miercoles 05 de Mayo del 2024 --------------------------------------------------


Algoritmo RenovacionLicencia
	Definir nombre, apellidoPaterno, apellidoMaterno, fechaNacimiento, numLicencia, formaPago, clavePago Como Caracter;
	Definir i, estadoPago Como Entero;
	// contadores inician de 0
	i := 0;
	estadoPago := 0;
	Mientras i < 2 Hacer
		// Datos ingresados y Valida que esten correctos
		Si i = 0 Entonces
			IngresoSistema
			// Ingresar los datos para despues validar que esten correctos
			Escribir "Ingrese su nombre:";
			Leer nombre;
			Escribir "Ingrese su apellido paterno:";
			Leer apellidoPaterno;
			Escribir "Ingrese su apellido materno:";
			Leer apellidoMaterno;
			Escribir "Ingrese su fecha de nacimiento iniciando por dia, mes y año";
			Leer fechaNacimiento;
			Escribir "Ingrese su número de licencia actual con formato DDMMYYYYGG:" ;
			Leer numLicencia;
			ValidarDatosPersonales(nombre, apellidoPaterno, apellidoMaterno, fechaNacimiento, numLicencia, i);
		FinSi
		// Ir a pagar la licencia
		Si i = 0 Entonces
			ProcesoDePago(estadoPago, clavePago, formaPago);
			estadoPago := 1;
		FinSi
		i := i + 1;
	FinMientras
	// Verificar límite de intentos
	Si i = 3 Entonces
		Escribir "Ha alcanzado el límite de intentos. El proceso se reiniciará más tarde";
	FinSi
	Si estadoPago = 1 Entonces
		Escribir "****************** Proceso de renovación completado ******************";
		Escribir "                          Datos del Cliente                    ";
		Escribir "El Ciudadano: ",nombre," ",apellidoPaterno," ",apellidoMaterno;
		// Funcion de fechaActual nos ayuda a sacar en automatico la fecha del mismo dia que se genera el pago
		Escribir "Con Numero de Licencia: ",numLicencia," ",", con Fecha de Pago: ",Subcadena(ConvertirATexto(FechaActual()),7,8),"/",Subcadena(ConvertirATexto(FechaActual()),5,6),"/",Subcadena(ConvertirATexto(FechaActual()),1,4);
		// Funcion de fechaActual mas 1 año para el vencimiento de la licencia en automatico
		Escribir "Fecha de Vencimiento: ",Subcadena(ConvertirATexto(FechaActual()),7,8),"/",Subcadena(ConvertirATexto(FechaActual()),5,6),"/",Subcadena(ConvertirATexto(FechaActual()+10000),1,4);
	FinSi
	Escribir "****************** Finalizo Su Proceso Hasta Luego *******************";
	Esperar 10 Segundos
	Borrar Pantalla
FinAlgoritmo


// Introducion al sistema para apartarlo de los subprocesos
SubProceso IngresoSistema
	//Introduccion al sistema
	Escribir "*********** Inicio del proceso de renovación de licencia. ************";
	Escribir "********************* Bienvenido a la plataforma *********************";
	Escribir "************ Por favor proporcione sus datos correctamente ***********";
	Escribir "**************** Escríbelos con Mayúsculas y Minúsculas **************";
FinSubProceso


// 1 Parte del Proceso de Renovacion
// Almacenamos la infromacion del usuario para despues validar
Subproceso ValidarDatosPersonales(nombre, apellidoPaterno, apellidoMaterno, fechaNacimiento, numLicencia, i)
	i := 0
	// Validamos cada uno de los valores que ingreso el usuario y los datos que no ingresen valores en null
	Mientras i < 2 Hacer
		Si nombre <> "" Entonces
			Si apellidoPaterno <> "" Entonces
				Si apellidoMaterno <> "" Entonces
					Si fechaNacimiento <> "" Entonces
						Si numLicencia <> "" Entonces
							Escribir "************************* Validando Nombre ***************************";
							Escribir "****************** Validando su apellido materno *********************";
							Escribir "****************** Validando su apellido materno *********************";
							Escribir "***************** Validando su fecha de nacimiento *******************";
							Escribir "****************** Validando numero de licencia **********************";
							Escribir "";
							barraCargaDoc
							Escribir "";
							Escribir "";
							Escribir "***************** Los datos son correctos y validados ****************";
							Esperar 2 Segundos
							i := 2
						SiNo
							Escribir "Su numero de licencia es incorrecto ingreselo nuevamente" ;
							Leer numLicencia;
							i := i + 1
						Fin Si
					SiNo
						Escribir "Su fecha de nacimiento es incorrecto ingreselo nuevamente";
						Leer fechaNacimiento;
						i := i + 1
					Fin Si
				SiNo
					Escribir "El apellido materno es incorrecto ingreselo nuevamente";
					Leer apellidoMaterno;
					i := i + 1
				Fin Si
			SiNo
				Escribir "El apellido paterno es incorrecto ingreselo nuevamente";
				Leer apellidoPaterno;
				i := i + 1
			Fin Si
		SiNo
			Escribir "El nombre es incorrecto ingreselo nuevamente";
			Leer nombre;
			i := i + 1
		FinSi
	FinMientras
	Esperar 1 Segundos
	Borrar Pantalla;
FinSubproceso


// 2 Parte del Proceso de Renovacion
// este es subpoceso que genera el pago y detona los subprocesos de validacion de cada metodo de pago
Subproceso ProcesoDePago(estadoPago, clavePago, formaPago)
	// Si los datos son correctos iniciara el proceso de pago validando la clave de pago y ingresando datos sea en efectivo o tarjeta
	// validando igualmente los metodos de pago con forme a los subprocesos
	Escribir "***************************** Bienvenido *****************************";
	Escribir "**************** Inicio el proceso de pago de licencia. **************";
	Escribir "";
	Escribir "Digita tu clave de pago con formato YYYYMMDDGG:";
	Leer clavePago;
	// si la clave no es correcta manda mensaje de que la clave es incorrecta
	Si clavePago = "20240311107" Entonces
		Escribir "El costo del pago es de 1850 pesos.";
		Escribir "¿Cómo deseas realizar el pago?";
		Escribir " 1 - Efectivo";
		Escribir " 2 - Tarjeta";
		Leer formaPago;
		Si formaPago = "1" o formaPago = "2" Entonces
			Si formaPago = "2" Entonces
				Escribir "Ingrese el número de tarjeta:";
				Leer numeroTarjeta;
				Escribir "Ingrese la fecha de vencimiento (MM/AA):";
				Leer fechaVencimiento;
				Escribir "Ingrese el código de seguridad (CVC):";
				Leer cvc;
				formaPago := "Tarjeta";
				// Validamos los valores de numero de tarjeta, fecha de vencimiento, cvc
				Si numeroTarjeta <> "" Y fechaVencimiento <> "" Y cvc <> "" Entonces
					Escribir "El pago con tarjeta tarda algunos minutos en reflejarse el pago";
					Escribir ""
					barraCargaDoc
					Escribir "";
					Escribir "";
					Escribir "***************** Los datos son correctos y validados ****************";
					Escribir "________________ Metodo de pago elegido es ",formaPago," _____________";
					Escribir "_____________________ Su licencia ha sido renovada ___________________";
					Escribir "_________________________ Su pago fue exitoso. _______________________";
				Sino
					Escribir "Datos de tarjeta inválidos. Por favor, inténtelo nuevamente.";
				FinSi
			Sino
				Escribir "Ingrese el numero de Folio:";
				Leer codigoFolio;
				formaPago := "Efectivo";
				// Valida los datos que se ingresan del pago en Efectivo como un metodo de adminitracion de folio por pago 
				Si codigoFolio <> "" Entonces
					Escribir "El pago con Efectivo se refleja en unos minutos";
					Escribir ""
					barraCargaDoc
					Escribir "";
					Escribir "";
					Escribir "***************** Los datos son correctos y validados ****************";
					Escribir "________________ Metodo de pago elegido es ",formaPago," _____________";
					Escribir "_____________________ Su licencia ha sido renovada ___________________";
					Escribir "_________________________ Su pago fue exitoso. _______________________";
				Sino
					Escribir "Datos de tarjeta inválidos. Por favor, inténtelo nuevamente.";
				FinSi
			FinSi
		SiNo
			Escribir "Forma de pago no válida.";
		FinSi    
	Sino
		Escribir "La clave de pago no es válida.";
	FinSi
	Esperar 5 Segundos;
	Borrar Pantalla;
FinSubproceso

SubProceso barraCargaDoc
	Para i <- 1 Hasta 100 Hacer
		Esperar 1 Segundos
		Escribir Sin Saltar "|||||||"
		i := i + 10
	FinPara	
FinSubProceso
	