import pandas

# Cargar el archivo CSV
datos = pandas.read_csv('Class 08/Estudiantes.csv')

# Mostrar las primeras filas
print (datos.head())

# filtrar en columnas "nombre" y "apellido"
print(datos[["nombre","apellido"]].head())

# Calcular estadisticas descriptivas
print(datos.describe())

# Calcular el maximo de la edad
print(datos['edad'].max())

# Minimo de edad
print(datos['edad'].min())

# filtrar estudiantes con calificación mayor a 85
estudiantes_alta_nota = datos[datos['nota']>85]
print(estudiantes_alta_nota)

# Agrupar por genero y calcular la media de las notas
media_por_genero = datos.groupby('sexo')
media_por_genero = media_por_genero['nota'].mean()
print (media_por_genero)
