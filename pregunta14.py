import os
import csv
from matplotlib import pyplot as plt

ruta = "./StopSearch_2011_2017/"
fecha = os.listdir(ruta) #diccionario los directorios que se encuentran dentro de la carpeta principal
tiposInspecciones = {} #diccionario para guardar los diferentes tipos de inspecciones encontrados


total = 0 #variable que cuenta el total de crímenes de cada archivo
for f in fecha: #recorre todos los directorios encontrados
	rutaSecundaria = ruta+f+"/" #se prepara la ruta donde se buscarán los archivos
	for e in os.listdir(rutaSecundaria): #se recorren todos los archivos encontrados en ese directorio
		archivo = open(rutaSecundaria+e) #se abre el archivo
		cLine = 0 #variable para que no cuente la primera línea, que es la del encabezado de cada archivo
		for line in archivo:
			if(cLine!=0):
				total+=1 #se incrementa el contador del total de inspecciones
				inspeccion = list(csv.reader([line.strip()],delimiter=','))[0][0] #separar la linea por comas y asi obtener el primer registro y guardarlo
				if(not(inspeccion in tiposInspecciones)): #Se compara si la inspección ya está en el diccionario de crímenes
					tiposInspecciones.update({inspeccion : 1 }) #En caso de no estarlo, se agrega al diccionario y se le da un valor de 1
				else:
					tiposInspecciones[inspeccion] += 1 #En caso de estarlo, solo se suma el contador de esa inspección
			cLine+=1





#_____________________Generar gráfica_____________________
tipoInspeccion = [] #Para guardar los diferentes tipos de inspecciones
porcentaje = [] #Para guardar el porcentaje de cada inspección


print("Total de inspecciones: ",total, "\n") #se imprime el total de inspecciones

#Se generan los resultados
for inspeccion in tiposInspecciones:
	#Se valida que el nombre del rango no esté vacío para no tomar en cuenta los registros faltantes
	if(inspeccion != ""):
		tipoInspeccion.append(inspeccion)
		porcentaje.append(round(((tiposInspecciones[inspeccion] * 100) / total),2))
		print(tipoInspeccion[-1], "=", porcentaje[-1])

plt.pie(porcentaje, labels=tipoInspeccion, colors=None, startangle=90, shadow=None, explode=None, autopct="%1.3f%%")
plt.title("Porcentaje de inspecciones por tipo de inspección")
plt.show()

