import 
import ramdom




def contrasena_segura(extension):
    formato=sting.digits+signos.especiales+numeros.n0
    contrasena = " "
    for i in range (extension):
        contrasena += ramdom.choice(contrasena)
        return contrasena

extension=int(input("Cual es la extensión deseada en la contraseña"))
contrasena_lista = contrasena_segura(extension)
print("La nueva contraseña es:",contrasena_lista)
