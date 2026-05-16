#Asignar valores a las variables,inicializar variables
nombre:str = "Alman"

#Solicitar al usuario su edad
edad:int = int(input("¿cuál es tu edad?"))

#Calcular año de naciiento
anno_de_nacimiento:int = 2026 - edad

#Imprimir nombre,edad y año de nacimiento
print ("Mi nombre es",nombre)
print ("Mi edad es",edad)
print ("Mi año de nacimiento es",anno_de_nacimiento)

#Calcular mayoria de edad
mayor_de_edad:bool = edad >= 18

#Imprimir mayoria de edad
print(mayor_de_edad)


#Inicializar variables
no_soy_yo = not(nombre == "Alman" and edad == 22 )
soy_yo = nombre=="Alman" and edad == 22
quizas_soy_yo = nombre == "Alman" or edad == 21

#Imprimir variables
print(no_soy_yo)
print(soy_yo)
print(quizas_soy_yo)

#Ejemplos de incrementos en variables nu´mericas
x = 10
x += 5

#imprimir resultado del ejemplo
print:(x)

