import os
import csv
from matplotlib import pyplot as plt

ruta = "./StopSearch_2011_2017/"
fecha = os.listdir(ruta) #diccionario los directorios que se encuentran dentro de la carpeta principal
gruposEtnicos = {} #diccionario para guardar los diferentes grupos étnicos encontrados


total = 0 #variable que cuenta el total de grupos étnicos de cada archivo
for f in fecha: #recorre todos los directorios encontrados
	rutaSecundaria = ruta+f+"/" #se prepara la ruta donde se buscarán los archivos
	for e in os.listdir(rutaSecundaria): #se recorren todos los archivos encontrados en ese directorio
		archivo = open(rutaSecundaria+e) #se abre el archivo
		cLine = 0 #variable para que no cuente la primera línea, que es la del encabezado de cada archivo
		for line in archivo:
			if(cLine!=0):
				total+=1 #se incrementa el contador del total de inspecciones
				grupoEtnico = list(csv.reader([line.strip()],delimiter=','))[0][9] #separar la linea por comas y asi obtener el registro y guardarlo
				if(not(grupoEtnico in gruposEtnicos)): #Se compara si el grupo étnico ya está en el diccionario de grupos étnicos
					gruposEtnicos.update({grupoEtnico : 1 }) #En caso de no estarlo, se agrega al diccionario y se le da un valor de 1
				else:
					gruposEtnicos[grupoEtnico] += 1 #En caso de estarlo, solo se suma el contador de ese grupo étnico
			cLine+=1





#_____________________Generar gráfica_____________________
grupos = [] #Para guardar los diferentes grupos étnicos
porcentajes = [] #Para guardar el porcentaje de cada inspección


print("Total de inspecciones: ",total, "\n") #se imprime el total de inspecciones

#Se generan los resultados
for grupoEtnico in gruposEtnicos:
	#Se valida que el nombre del grupo étnico no esté vacío para no tomar en cuenta los registros faltantes
	if(grupoEtnico != ""):
		grupos.append(grupoEtnico)
		porcentajes.append(round(((gruposEtnicos[grupoEtnico] * 100) / total),2))
		print(grupos[-1], "=", porcentajes[-1])

#Se cambian algunos valores para que la gráfica sea legible
grupos[0], grupos[1] = grupos[1], grupos[0]
porcentajes[0], porcentajes[1] = porcentajes[1], porcentajes[0]

plt.pie(porcentajes, labels=grupos, colors=None, startangle=90, shadow=None, explode=None, autopct="%1.3f%%")
plt.title("Porcentaje de inspecciones por grupo étnico")
plt.show()
