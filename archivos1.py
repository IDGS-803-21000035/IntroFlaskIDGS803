from io import open

#(nombre del archivo, modo de apertura), el modo a crea el archivo si no existe
archivo_texto = open('nombres.txt', 'a')

#escribo en el archivo
#archivo_texto.write('\n datos en el archivo')

#Despues de usarlo de sebe cerrar
#archivo_texto.close()

#Arir archivo para lectura
archivo_texto = open('nombres.txt','r')

#print(archivo_texto.read())

# -------- Manejo del punturo ----------
#Apartir de la posicion 0 lee hacia delante
#archivo_texto.seek(0)
#print(archivo_texto.read())

#Lee linea
#print(archivo_texto.readline())

#HAce una lista de todas las lineas del archivo
#print(archivo_texto.readlines())

for lines in archivo_texto.readlines():
    print(lines.rsplit())

#Despues de usarlo de sebe cerrar
archivo_texto.close()
