import random

# Variables
cantidadDeMuestras = 4
albumCompleto = False
sobresAbiertos = 0
album = []
sobre = []
muestra = []

# Lleno el album todo vacio
for a in range(0, 99):
    album.append(False)

#abrir sobre
def abrirSobre():
    for s in range(0,5):
        sobre.append(random.randint(0, 98))
    return sobre

#ingresar sobre en album
def pegarFigAlbum():
    sobre = abrirSobre()
    global sobresAbiertos
    sobresAbiertos += 1
    for numeroFigurita in sobre:
        album[numeroFigurita] = True

def checkearAlbumCompleto():
    global albumCompleto
    if False in album:
       albumCompleto = False
    else:
        albumCompleto = True
        albumCompleto += 1

while albumCompleto == False:
    pegarFigAlbum()
    checkearAlbumCompleto()

if albumCompleto == True:
    print(sobresAbiertos)

for m in range(0, cantidadDeMuestras):
    muestra.append(sobresAbiertos)

print (muestra)




#    no puedo hacer que vaya grabando cada iteracion a la fila muestra!



