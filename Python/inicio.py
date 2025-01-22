cuentas = {}

while True:
    agregar = input("Ingrese la cuenta que quiere agregar (ingrese -1 para salir):\n")
    while agregar in cuentas:
        agregar = input("Ya se encuentra. Ingrese la cuenta que quiere agregar (ingrese -1 para salir):\n")
    if agregar == "-1":
        break
    contra = input(f"Ingrese la contraseña de {agregar}:\n")
    cuentas[agregar] = contra
    print(f"Se agrego la cuenta {agregar}!")

ingresar = input("A que cuenta quiere ingresar? Con -1 se va.\n")
while ingresar not in cuentas and ingresar != "-1":
    ingresar = input("Usuario inexistente. A que cuenta quiere ingresar? (con -1 salis)\n")

if ingresar != "-1":
    for i in range(1,4):
        contra = input(f"Ingrese la contraseña de {ingresar}, tiene 3 intentos (Intento numero {i}):\n")
        if contra == cuentas[ingresar]:
            print("Ingreso correctamente!")
            break
        else:
            print(f"Contraseña incorrecta.")
else:
    print("No entro a ninguna cuenta.")