#Juego del Ahorcado
# Importación de la librería random con todos sus métodos/funciones.
from random import *

palabras=["uno","vino","pera","verano","eñe"]
auxiliar=[]
palabra = list(palabras[0]) #En este apartado se pondrá para que elija la palabra aleatoriamente
for i in range(len(palabra)):
    auxiliar.append("_") #Aquí creamos la palabra oculta con el número total de letras que contendrá.
#print(auxiliar)
#print(palabra) #Esto es solo comprobación
print("Dime una letra")
letra = input()
print(letra) #Esto es solo comprobación
for i in range(len(palabra)):
    if letra == palabra[i]:
        auxiliar[i] = letra
        print("Letra correcta")
    else:
        print("La letra no está en esta palabra")
print("La palabra es: ", auxiliar)
    
