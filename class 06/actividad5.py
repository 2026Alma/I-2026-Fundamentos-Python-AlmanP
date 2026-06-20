def consultar(saldo):
    print(F"Su saldo es:{saldo}")

def depositar(saldo, cantidad):
    resultado = saldo + cantidad
    return resultado

def retirar(saldo):
    cantidad = int(input("Ingese la cantidad a retirar:"))
    if cantidad > saldo :
        print ("No tiene suficiente saldo")
        return saldo
        else:
        saldo = saldo - cantidad
        print (f"Ha retirado: {cantidad}")
        return saldo

print("Cajero Automatico")

print ("Bienvenido a su cajero automatico")

saldo = 0
while True:
    print("1:Consultar saldo")
    print("2:Retirar dinero")
    print("3:Depositar dinero")
    print("4:Salir")
    opcion = int (input("Seleccione una opcion"))
    if opcion == 1:
        consultar(saldo)
    elif opcion == 2:
        saldo = retirar(saldo)
    elif opcion == 3:
        cantidad=int(input("Ingrese la cantidad a depositar:"))
        saldo = depositar(saldo, cantidad)
        print(f"Ha depositado:{cantidad}")
    
    elif opcion == 4:
        print ("Gracias por usar el cajero automático")
        break

    else:
        print("Opcion incorrecta,ingrese de nuevo una opcion")



