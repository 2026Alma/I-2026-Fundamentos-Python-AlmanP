#1 Crear clase
class Vehiculo:
    def __init__ (self, Placa, Marca, Año):
        self.Placa = Placa
        self.Marca = Marca
        self.Año = Año

    def mostrar(self):
        print(self.Placa, self.Marca, self.Año)

#2 Solicitar información

registrar_vehiculos = int(input("Cuántos vehículos desea registrar: "))

#Registrar información
vehiculos = []
for i in range(registrar_vehiculos):
    Placa = str(input("Ingrese la placa de su vehículo: "))
    Marca = str(input("Ingrese la marca de su vehículo: "))
    Año = int (input("Ingrese el año de su vehículo: "))
    vehiculo = Vehiculo(Placa, Marca, Año)
    vehiculos.append(vehiculo)

# 4.Mostrar Resultados
for vehiculo in vehiculos:
    vehiculo.mostrar()
    
                    

