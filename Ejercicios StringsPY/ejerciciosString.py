#1

ejemplo = "  Me gusta Java"
print (ejemplo)
#2

txtMayus = ejemplo.upper()
print (txtMayus)

#3

txtSinEspacios = ejemplo.strip()
print(txtMayus)

#4

txtMinus = ejemplo.lower()
print(txtMinus)

#5

if txtMayus == txtMinus:
    print("Son iguales")
else:
    print("Son diferentes")

#6 #7 #8

cad1 = "aaaaaabbbbbccccc"
cad2 = "bbbbccccdddd"

if cad1 < cad2:
    print(f"{cad1} es anterior a {cad2}")
else:
    print (f"{cad2} es anterior a {cad1}")

#9
ejemplo2 = "En un lugar de la Mancha"

contiene = ejemplo2.find("M")

if contiene == -1:
    print("no la contiene")
else:
    print(f"la contiene en la posición {contiene}")

#10
print(ejemplo2[6:11])

#11

frase = ("dabale arroz a la zorra el abad")
frase_al_reves = frase[::-1]
print(frase_al_reves)

#12 

fraseEspacio= "Estoy estudiando Java en el IES Camp de Morvedre"

print (fraseEspacio.replace(" ", ""))

#13

fraseUnida = ("www.google.es")

fraseSeparada= print (fraseUnida [0:10])

fraseSeparada2= print (fraseUnida [10:])
