import os
import csv
from matplotlib import pyplot as plt

ruta = "./StopSearch_2011_2017/"
fecha = os.listdir(ruta) #diccionario los directorios que se encuentran dentro de la carpeta principal
rangosEdades = {} #diccionario para guardar los diferentes tipos de rangos de edad encontrados


total = 0 #variable que cuenta el total de rangos de edad de cada archivo
for f in fecha: #recorre todos los directorios encontrados
	rutaSecundaria = ruta+f+"/" #se prepara la ruta donde se buscarán los archivos
	for e in os.listdir(rutaSecundaria): #se recorren todos los archivos encontrados en ese directorio
		archivo = open(rutaSecundaria+e) #se abre el archivo
		cLine = 0 #variable para que no cuente la primera línea, que es la del encabezado de cada archivo
		for line in archivo:
			if(cLine!=0):
				total+=1 #se incrementa el contador del total de inspecciones
				rangoEdad = list(csv.reader([line.strip()],delimiter=','))[0][7] #separar la linea por comas y asi obtener el primer registro y guardarlo
				if(not(rangoEdad in rangosEdades)): #Se compara si el rango de edad ya está en el diccionario de rangos de edad
					rangosEdades.update({rangoEdad : 1 }) #En caso de no estarlo, se agrega al diccionario y se le da un valor de 1
				else:
					rangosEdades[rangoEdad] += 1 #En caso de estarlo, solo se suma el contador de ese rango de edad
			cLine+=1





#_____________________Generar gráfica_____________________
rangos = [] #Para guardar los diferentes rangos de edades
porcentajes = [] #Para guardar el porcentaje de cada inspección


print("Total de inspecciones: ",total, "\n") #se imprime el total de inspecciones

#Se generan los resultados
for rangoEdad in rangosEdades:
	#Se valida que el nombre del rango no esté vacío para no tomar en cuenta los registros faltantes
	if(rangoEdad != ""):
		rangos.append(rangoEdad)
		porcentajes.append(round(((rangosEdades[rangoEdad] * 100) / total),2))
		print(rangos[-1], "=", porcentajes[-1])

plt.pie(porcentajes, labels=rangos, colors=None, startangle=90, shadow=None, explode=None, autopct="%1.3f%%")
plt.title("Porcentaje de inspecciones por rango de edad")
plt.show()
