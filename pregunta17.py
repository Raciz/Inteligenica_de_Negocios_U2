import os
import csv
from matplotlib import pyplot as plt

ruta = "./StopSearch_2011_2017/"
fecha = os.listdir(ruta) #diccionario los directorios que se encuentran dentro de la carpeta principal
generos = {} #diccionario para guardar los diferentes géneros encontrados


total = 0 #variable que cuenta el total de géneros de cada archivo
for f in fecha: #recorre todos los directorios encontrados
	rutaSecundaria = ruta+f+"/" #se prepara la ruta donde se buscarán los archivos
	for e in os.listdir(rutaSecundaria): #se recorren todos los archivos encontrados en ese directorio
		archivo = open(rutaSecundaria+e) #se abre el archivo
		cLine = 0 #variable para que no cuente la primera línea, que es la del encabezado de cada archivo
		for line in archivo:
			if(cLine!=0):
				total+=1 #se incrementa el contador del total de inspecciones
				genero = list(csv.reader([line.strip()],delimiter=','))[0][6] #separar la linea por comas y asi obtener el registro y guardarlo
				if(not(genero in generos)): #Se compara si el género ya está en el diccionario de géneros
					generos.update({genero : 1 }) #En caso de no estarlo, se agrega al diccionario y se le da un valor de 1
				else:
					generos[genero] += 1 #En caso de estarlo, solo se suma el contador de ese género
			cLine+=1





#_____________________Generar gráfica_____________________
generosL = [] #Para guardar los diferentes géneros sexuales
porcentajes = [] #Para guardar el porcentaje de cada inspección


print("Total de inspecciones: ",total, "\n") #se imprime el total de inspecciones

#Se generan los resultados
for genero in generos:
	#Se valida que el nombre del género no esté vacío para no tomar en cuenta los registros faltantes
	if(genero != ""):
		generosL.append(genero)
		porcentajes.append(round(((generos[genero] * 100) / total),2))
		print(generosL[-1], "=", porcentajes[-1])

fig = plt.figure("Porcentaje de inspecciones por género")
ax = fig.add_subplot(111)
xx = range(1, len(porcentajes)+1)

ax.bar(xx, porcentajes, width=0.8,  color=['blue','red','green','orange','brown','purple','pink'], align="center")
ax.set_xticks(xx)
ax.set_xticklabels(generosL)
ax.set_ylabel("Crímenes")

plt.xlabel("Géneros")
plt.ylabel("Porcentaje")

#Se muestra el valor de cada barra en la gráfica
for i,v in enumerate(porcentajes):
	plt.text(i+0.85, v+2, str(v)+"%", color='black', va='center', fontweight='bold')



plt.show()
