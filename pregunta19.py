import os
from matplotlib import pyplot as plt
import csv


ruta = "./CrimesUK_2011_2017/"
fecha = os.listdir(ruta) #lista los directorios que se encuentran dentro de la carpeta principal
fecha.sort() #ordena el arreglo del año menor al mayor 

i = 0 #para saber en que año va
years = [] #agregar el total del año al arreglo
anual = 0 #contar el total por año

#lista con el nombre de las fuerza policiacas
forces = os.listdir("./CrimesUK_2011_2017/2011-01")

#borramos lo necesario para quedarnos solo con el nombre de la fuerza
for i in range(len(forces)):
    forces[i] = forces[i][8:-11]
    
forces.sort()

crimenesFuerza = [0]*42
"""resultados = open("datos_faltantes.txt", "w")
for f in fecha:
	rutaSecundaria = ruta+f+"/"
	fuerza = 0
	archivos = os.listdir(rutaSecundaria)
	archivos.sort()
	for e in archivos:
		faltantes = 0
		archivo = open(rutaSecundaria+e) #abrir el archivo
		cLine = 0 #variable para que no cuente la primera línea, que es la del encabezado de cada archivo
		for line in archivo:
			if(cLine!=0):
				for r in range(12):
					if(list(csv.reader([line.strip()],delimiter=','))[0][r]==""):
						faltantes+=1
			cLine+=1
		crimenesFuerza[fuerza] += faltantes
		fuerza+=1
		
for l in range(len(crimenesFuerza)):
	resultados.write(str(crimenesFuerza[l]))
	resultados.write('\n')"""
		
archivoDatos = open("./datos_faltantes.txt")
i=0
for line in archivoDatos:
	crimenesFuerza[i] = line.split(" ")[0]
	i+=1

plt.title("Cantidad de datos faltantes por Fuerza Policiaca")
num = [y for y in range(len(forces))]
plt.plot(num, crimenesFuerza, 'r*-');
xx = range(0, len(forces))
plt.xticks(xx, forces, rotation=90)
plt.grid(True)
plt.xlabel("Fuerzas policiacas")
plt.ylabel("Cantidad de datos faltantes")
plt.show()
