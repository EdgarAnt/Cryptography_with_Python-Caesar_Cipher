#Lectura de archivos de caracter a caracter Mi_cancion_favorita
name = input("Nombre del archivo: ")
archivo = open(name + ".txt", "r")
carac = archivo.read(1)
suma = 1
codificador = " "
abc = "abcdefghijklmnopqrstuvwxyz"

for linea in archivo:
    for l in linea:
        if l in abc:
            ind = abc.find(l)
            ind += 1
            if ind >= 26:
                ind -= 26
            codificador += abc[ind]
        else:
           codificador += l

print(codificador, end="")
archivo.close()
archivo = open(name + ".txt", "r")
while carac != "":
    carac = archivo.read(1)
    suma += 1#contador de caracteres
print("\n--------------------------------")
print(f'Cantidad de palabras es: {suma}')#Imprime la cantidad a mostrar al usar el contador
print("--------------------------------")

archivo.close()
