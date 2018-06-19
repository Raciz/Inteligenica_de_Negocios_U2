import os
import csv
import numpy as np
from matplotlib import pyplot as plt

#Función para sacer el mes y el año de la fecha
def getMes(fecha):
	#Se divide la fecha y se devuelve el campo de mes y del año
	return int(list(csv.reader([fecha.strip()],delimiter='-'))[0][1]), int(list(csv.reader([fecha.strip()],delimiter='-'))[0][0])


ruta = "./StopSearch_2011_2017/"
fecha = os.listdir(ruta) #diccionario los directorios que se encuentran dentro de la carpeta principal

#Arreglo para guardar el número de inspecciones de cada mes por año
reportes = [
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #2014
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #2015
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #2016
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #2017
]


total = 0 #variable que cuenta el total de meses de cada archivo
for f in fecha: #recorre todos los directorios encontrados
	rutaSecundaria = ruta+f+"/" #se prepara la ruta donde se buscarán los archivos
	for e in os.listdir(rutaSecundaria): #se recorren todos los archivos encontrados en ese directorio
		archivo = open(rutaSecundaria+e) #se abre el archivo
		cLine = 0 #variable para que no cuente la primera línea, que es la del encabezado de cada archivo
		for line in archivo:
			if(cLine!=0):
				total+=1 #se incrementa el contador del total de inspecciones
				fecha = list(csv.reader([line.strip()],delimiter=','))[0][1] #separar la linea por comas y asi obtener la fecha
				mes, anio = getMes(fecha) #Se saca el mes y el año de esa fecha
				reportes[anio - 2014][mes-1] += 1	#Se aumenta la cantidad de reportes de ese año y ese mes

			cLine+=1


print("Total de inspecciones: ",total, "\n") #se imprime el total de inspecciones

#Se imprimen los resultados
for i in range(len(reportes)):
	print("***Año", 2014 + i, "***")
	for j in range(len(reportes[i])):
		print(j+1, ":", reportes[i][j])
	print("\n\n")


meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"] #Nombres de los meses
mesesY = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #Para guardar el promedio de cada mes

#Para guardar los valores de los meses y poder sacar la desviación estándar
mesesY2 = [
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0]
]

desviacionStd = [] #Desviación estándar de los meses

#Se recorre el arreglo de reportes
for i in range(len(reportes)):
	for j in range(len(reportes[i])):
		mesesY[j] += reportes[i][j] #Se va acumulando el total de reportes de cada mes
		mesesY2[j][i] += reportes[i][j] #Se va llenando la matriz transpuesta de los reportes

#Para sacar el promedio de cada mes
for i in range(len(mesesY)):
	if i == 0 or i == 1:
		mesesY[i] = int(mesesY[i] / 3) #Si es enero o febrero se divide entre 3
	else:
		mesesY[i] = int(mesesY[i] / 4) #Si no se divide entre 4


#Se saca la desviación estándar para cada mes
for i in range(len(mesesY2)):
	desviacionStd.append(np.std(mesesY2[i]))

print("Promedios:") 
for i in range(12):
	print(mesesY[i])


print("\nDesviación Std:") 
for i in range(12):
	print(desviacionStd[i])



#Gráfica
fig = plt.figure("Promedio de reportes por mes")
ax = fig.add_subplot(111)
xx = range(1, len(mesesY)+1)

ax.bar(xx, mesesY, width=0.8,  color=['blue','red','green','orange','brown','purple','pink'], align="center", yerr=desviacionStd)
ax.set_xticks(xx)
ax.set_xticklabels(meses)
ax.set_ylabel("Crímenes")

plt.xlabel("Meses")
plt.ylabel("Promedio")

#Se muestra el valor de cada barra en la gráfica
for i,v in enumerate(mesesY):
	plt.text(i+0.67, v, str(v), color='black', va='center', fontweight='bold')



plt.show()
