perro = "perro feliz"
perro2 = "   perro feliz  "

print (perro.upper()) # todo en mayusculas o el caracter que elijamos perro[1].upper()
print (perro.lower()) # todo en minusculas o el caracter que elijamos perro[1].lower()
print (perro.capitalize()) # La primera letra a mayusculas()
print (perro.title()) # La primera letra de cada palabra a mayusculas()
print (perro2.strip()) # Elimina espacios de ambos lados
print (perro2.lstrip()) # Elimina espacios de la izquierda
print (perro2.rstrip()) # Elimina espacios de la derecha
#podemos combinarr estos metodos
print (perro2.strip().upper()) # Elimina espacios de ambos lados y lo pone en mayusculas    
print (perro.find("e"))