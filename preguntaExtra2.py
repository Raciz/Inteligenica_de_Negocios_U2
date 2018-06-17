import os
import csv
from matplotlib import pyplot as plt

ruta = "./StopSearch_2011_2017/"
fecha = os.listdir(ruta) #diccionario los directorios que se encuentran dentro de la carpeta principal
acciones = {} #diccionario para guardar las diferentes acciones encontradas


total = 0 #variable que cuenta el total de acciones de cada archivo
for f in fecha: #recorre todos los directorios encontrados
	rutaSecundaria = ruta+f+"/" #se prepara la ruta donde se buscarán los archivos
	for e in os.listdir(rutaSecundaria): #se recorren todos los archivos encontrados en ese directorio
		archivo = open(rutaSecundaria+e) #se abre el archivo
		cLine = 0 #variable para que no cuente la primera línea, que es la del encabezado de cada archivo
		for line in archivo:
			if(cLine!=0):
				total+=1 #se incrementa el contador del total de acciones 
				accion = list(csv.reader([line.strip()],delimiter=','))[0][12] #separar la linea por comas y asi obtener el registro y guardarlo
				if(not(accion in acciones)): #Se compara si la acción ya está en el diccionario de acciones
					acciones.update({accion : 1 }) #En caso de no estarlo, se agrega al diccionario y se le da un valor de 1
				else:
					acciones[accion] += 1 #En caso de estarlo, solo se suma el contador de esa acción
			cLine+=1





#_____________________Generar gráfica_____________________
accionesL = [] #Para guardar los diferentes acciones realizadas después de cada inspección
porcentajes = [] #Para guardar el porcentaje de cada inspección


print("Total de inspecciones: ",total, "\n") #se imprime el total de inspecciones

#Se generan los resultados
for accion in acciones:
	#Se valida que el nombre de la acción no esté vacío para no tomar en cuenta los registros faltantes
	if(accion != ""):
		accionesL.append(accion)
		porcentajes.append(round(((acciones[accion] * 100) / total),3))
		print(accionesL[-1], "=", porcentajes[-1], "-", acciones[accion])

plt.barh(accionesL, porcentajes, color=['blue','red','green','orange','brown','purple','pink'], )
plt.title("Acciones realizadas después de cada inspección")
plt.xlabel("Porcentaje")
plt.ylabel("Acciones realizadas")

#Se ordenan manualmente los porcentajes que se mostrarán en la gráfica
porcentajes2 = porcentajes
porcentajes2[0], porcentajes2[1], porcentajes2[2], porcentajes2[3], porcentajes2[4], porcentajes2[5], porcentajes2[6], porcentajes2[7], porcentajes2[8], porcentajes2[9], porcentajes2[10], porcentajes2[11], porcentajes2[12], porcentajes2[13], porcentajes2[14], porcentajes2[15] = porcentajes2[9], porcentajes2[8], porcentajes2[5], porcentajes2[14], porcentajes2[12], porcentajes2[11], porcentajes2[2], porcentajes2[0], porcentajes2[7], porcentajes2[3], porcentajes2[6], porcentajes2[13], porcentajes2[10], porcentajes2[4], porcentajes2[1], porcentajes2[15] 

#Se muestra el valor de cada barra en la gráfica
for i,v in enumerate(porcentajes2):
	plt.text(v, i, str(v)+"%", color='black', va='center', fontweight='bold')

plt.show()
