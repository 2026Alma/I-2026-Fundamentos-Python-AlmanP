

print( "Bienvenido a su Registro estudiantil")


while True:
    print("1:Registrar estudiante")
    print("2:Imprimir estudiantes")
    print("3:Salir")
    opcion = int(input("Seleccione una opcion"))
    if opcion == 1:
        archivo = open ("C:\\Users\Persona Invitada\\Desktop\\1-2026-Fundamentos-Python-AlmanP\\class 06\\estudiantes.txt", "a")
        Nombre = str(input("Ingrese nombre: ",))
        Carne = int(input("Digite su carne: "))
        Nota = int(input("Resultado:"))
        archivo.write(f"{Nombre},{Carne},{Nota}")
        archivo.close()
    elif opcion == 2: 
        print(f"estudiante ingresado:", (Nombre), (Carne), (Nota))
    
    elif opcion == 3:
         print ("Gracias por su registro")
         break

    else :
        print("Siga el siguiente formato;nombre luego nueve digitos respectivos de carne y su nota final")


        







