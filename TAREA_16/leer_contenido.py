#realizo dos formas de realizar la lectura

#se realiza la lectura de archivo
datos=open("my_notes.txt", "r")
linea1=datos.readline()
linea2=datos.readline()
linea3=datos.readline()
linea4=datos.readline()
linea5=datos.readline()
linea6=datos.readline()

#imprimir linea por linea
print(linea1)
print(linea2)
print(linea3)
print(linea4)
print(linea5)
print(linea6)

#cerrar el archivo
datos.close()



# Lectura de archivo de texto utilizando with

with open('my_notes.txt', 'r') as file:
    # Leer y mostrar cada línea del archivo
    for line in file:
        print(line, end='')

# El archivo se cierra automáticamente al usar'with'








