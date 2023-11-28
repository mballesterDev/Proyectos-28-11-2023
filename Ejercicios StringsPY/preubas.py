nombreCurso = "Python"
descripcion = """Estamos aprendiendo Python al maximo, vamos a ser los mejroes prograamdores del mundo
lo juro"""

# Remover los espacios de la cadena
descripcion_sin_espacios = descripcion.replace(" ", "")

# Contar la longitud de la cadena sin espacios
longitud_descripcion_sin_espacios = len(descripcion_sin_espacios)

print(longitud_descripcion_sin_espacios)

print(nombreCurso[0:5])  # IRA DESDE LA POSICION 0 HASTA LA 5

print(nombreCurso[:5])  # IRA DESDE LA POSICION 5 A LA 0

print(nombreCurso[5:])  # IRA DESDE LA POSICION 5 A LA final

# OPERADOR DE FORMATEO DE CADENAS

nombre = "Manel"
apellido = "Ballester"

# dentro de {} puedes poner lo que quieras

# nombreCompleto = "Manel Ballester"
nombreCompleto = f"{nombre} {apellido}"
print(nombreCompleto)

inicialesNombre = f"{nombre[0]} {apellido[0]}"
print(inicialesNombre)

random = f"{nombre} {2+2} "
print(random)
