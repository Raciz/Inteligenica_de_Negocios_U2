import os
import re
import math
import csv
from matplotlib import pyplot as plt

EARTH_RADIUS_KM = 6371.0

#Función para eliminar las etiquetas de un string
def eliminarEtiquetas(texto):
	regExp = re.compile("<.*?>") #Expresión regular que identifica las etiquetas
	nvoTexto = re.sub(regExp, " ", texto) #El texto se "limpia" y se pasa a un nuevo string
	return nvoTexto #Se retorna el string limpio



crimenesFueraArea = {} #diccionario para guardar los crímenes registrados fuera del área de cobertura de cada fuerza policiaca

ruta = "./PoliceForce_KML/" #Ruta en la que se encuentran los archivos KML
archivos = os.listdir(ruta) #Lista de archivos KML
archivos.sort() #Se ordenan los archivos

ruta2 = "./CrimesUK_2011_2017/" #Ruta de los archivos principales
directorios = os.listdir(ruta2) #lista los directorios que se encuentran dentro de la carpeta principal

#Ciclo para recorrer los archivos. Para cada fuerza policiaca...
for f in archivos:
	nombreFuerza = os.path.splitext(f)[0] #Se obtiene el nombre de la fuerza policiaca
	totalReportes = 0 #Contador de crímenes reportados por la fuerza
	archivo = open(ruta + f) #Se abre el archivo "f" del directorio

	latitudes = [] #Lista para guardar las latitudes
	longitudes = [] #Lista para guardar las longitudes

	i = 0 #Contador de líneas
	#Ciclo para recorrer el archivo
	for line in archivo:
		#Si se ha llegado a la línea 13 (la que contiene las coordenadas)
		if i == 13:
			coordenadasTotales = eliminarEtiquetas(line).split() #Se eliminan las etiquetas de esa línea y las coordenadas se guardan en una lista

			#Se recorre la lista de coordenadas
			for coordenadas in coordenadasTotales:
				coordenadas2 = coordenadas.split(",") #El string de las coordenadas se separa para guardar por separado la latitud y la longitud 
				longitudes.append(float(coordenadas2[0])) #Se guarda la longitud actual en valor decimal
				latitudes.append(float(coordenadas2[1])) #Se guarda la latitud actual en valor decimal

			latitudes.sort() #Se ordenan las latitudes
			longitudes.sort() #Se ordenan las longitudes
		
			x1, x2 = latitudes[0], latitudes[-1] #Se sacan los puntos de menor y mayor latitud
			y1, y2 = longitudes[0], longitudes[-1] #Se sacan los puntos de menor y mayor longitud

			#Ciclo para recorrer los archivos de reportes principales
			for f2 in directorios:
				rutaSecundaria = ruta2+f2+"/" #se prepara la ruta donde se buscarán los archivos

				#se recorren todos los archivos encontrados en ese directorio
				for e in os.listdir(rutaSecundaria):
					#Se comprueba que el archivo sea el de los reportes de la fuerza policiaca actual
					if e.find(nombreFuerza) != -1:
						archivo = open(rutaSecundaria+e) #se abre el archivo
						
						cLine = 0 #variable para que no cuente la primera línea, que es la del encabezado de cada archivo
						#Se recorre el archivo
						for line in archivo:
							if(cLine!=0):
								totalReportes += 1 #Se aumenta el número de crímenes reportados
								latitud = list(csv.reader([line.strip()],delimiter=','))[0][5] #separar la linea por comas y asi obtener la latitud
								longitud = list(csv.reader([line.strip()],delimiter=','))[0][4] #separar la linea por comas y asi obtener la longitud

								#Se comprueba que el dato no esté vacío
								if latitud != "" and longitud != "":
									#Se comprueba si las coordenadas del crimen están fuera del área de cobertura de la fuerza policiaca
									if float(latitud) < float(x1) or float(latitud) > float(x2) or float(longitud) < float(y1) or float(longitud) > float(y2):
										#Se compara si la fuerza policiaca ya está en la diccionario de fuerzas policiacas
										if(not(nombreFuerza in crimenesFueraArea)):
											crimenesFueraArea.update({nombreFuerza : {"crimenesFuera" : 1} }) #En caso de no estarlo, se agrega a la diccionario y se le da un valor de 1
										else:
											crimenesFueraArea[nombreFuerza]["crimenesFuera"] += 1 #En caso de estarlo, solo se suma el contador de esa fuerza policiaca

							cLine+=1

						break #Se rompe el ciclo, ya no es necesario verificar los demás archivos

			break #Se rompe el ciclo, ya no es necesario verificar las demás líneas

		i += 1 #Se aumenta el contador

	crimenesFueraArea[nombreFuerza].update({"totalReportes" : totalReportes}) #Se agrega al diccionario en la fuerza actual el total de reportes


for i in crimenesFueraArea:
	print(i, ":", crimenesFueraArea[i])





#_____________________Generar gráfica_____________________
fuerzas = [] #Para guardar los nombres de las fuerzas policiacas
totales = [] #Para guardar el total de cada fuerza policiaca
porcentajes = [] #Para guardar el porcentaje de cada fuerza policiaca
totalesFuerzas = [] #Para guardar el total de cada fuerza policiaca


#Se generan los resultados
for fuerza in crimenesFueraArea:
	fuerzas.append(fuerza)
	totales.append(crimenesFueraArea[fuerza]["crimenesFuera"])
	totalesFuerzas.append(crimenesFueraArea[fuerza]["totalReportes"])
	porcentajes.append(round(((crimenesFueraArea[fuerza]["crimenesFuera"] * 100) / crimenesFueraArea[fuerza]["totalReportes"]),4))
	print(fuerzas[-1], "=", porcentajes[-1], ",", totales[-1])

plt.barh(fuerzas, porcentajes, color=['blue','red','green','orange','brown','purple','pink'])
plt.title("Crímenes reportados por las fuerzas fuera de su área de cobertura")
plt.xlabel("Porcentaje")
plt.ylabel("Fuerzas policiacas")

#Se muestra el valor de cada barra en la gráfica
for i,v in enumerate(porcentajes):
	plt.text(v, i, str(v)+"%", color='black', va='center', fontweight='bold')

plt.show()






#11:32 - 11:50

