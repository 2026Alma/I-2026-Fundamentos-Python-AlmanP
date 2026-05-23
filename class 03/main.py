print ("Bienvenido a su calculadora IMC")

#Solicitar nombre de usuario
nombre: str=(input("Nombre del usuario"))

#apellidos del usuario
apellidos: str = (input("Brinde sus apellidos"))

#edad del usuario
edad : int = int(input("Brinde su edad"))

#debe solicitar el peso del usuario
peso : float =float(input("Brinde su peso"))

#Altura
altura : float =float(input("Brinde su altura"))

#calcular el IMC
imc=peso/(altura**2)
clasificacion = ""
if imc < 18.5 :
    clasificacion="Bajo peso"
elif imc < 24.9 :
    clasificacion= "Peso normal"
elif imc < 29.9 :
    clasificacion= "Sobrepeso"
elif imc>=30:
    clasificacion="Obesidad"

print("Nombre: ", nombre,apellidos ) 
print("edad:",edad)
print("IMC:",imc)
print("clasificacion:",clasificacion)



