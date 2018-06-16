import os

ruta = "./CrimesUK_2011_2017/"
fecha = os.listdir(ruta) #lista los directorios que se encuentran dentro de la carpeta principal

total = 0 #variable que cuenta el total de crímenes de cada archivo
for f in fecha: #recorre todos los directorios encontrados
	rutaSecundaria = ruta+f+"/" #se prepara la ruta donde se buscarán los archivos
	for e in os.listdir(rutaSecundaria): #se recorren todos los archivos encontrados en ese directorio
		archivo = open(rutaSecundaria+e) #se abre el archivo
		cLine = 0 #variable para que no cuente la primera línea, que es la del encabezado de cada archivo
		for line in archivo:
			if(cLine!=0):
				total+=1 #se incrementa el contador del total de crímenes
			cLine+=1
			
print("Total de crímenes: ",total) #se imprime el resultado
