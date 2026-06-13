archivo = open ("C:\\Users\\Persona Invitada\\Desktop\\1-2026-Fundamentos-Python-AlmanP\\class 06\\estudiantes.txt", "a")
nombre= str(input("Ingrese su nombre"))
Carne=int(input("N. de carne"))
Nota =int (input("Nota final"))
archivo.write(f"{nombre},{Carne},{Nota}")
archivo.close()
while True:
    print("1:Registrar estudiante")
    print("2:Imprimir estudiantes")
    print("3:Salir")
    opcion = int(input("Seleccione una opcion"))
    if opcion == 1
      print(nombre)

