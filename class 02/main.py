nombre:str = "Alman"
edad:int = int(input("¿cuál es tu edad?"))
anno_de_nacimiento:int = 2026 - edad
print(anno_de_nacimiento)
mayor_de_edad:bool = edad >= 18
print(mayor_de_edad)

no_soy_yo = not(nombre == "Alman" and edad == 22 )
soy_yo = nombre=="Alman" and edad == 22
quizas_soy_yo = nombre == "Alman" or edad == 21

print(no_soy_yo)
print(soy_yo)
print(quizas_soy_yo)

x = 10
x += 5
print(x)

