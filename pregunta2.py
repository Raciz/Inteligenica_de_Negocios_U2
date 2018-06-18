import os
from matplotlib import pyplot as plt
#import csv
#print(list(csv.reader([line.strip()],delimiter=','))[0]) #separar la linea por comas y asi obtener los registros

ruta = "./CrimesUK_2011_2017/"
fecha = os.listdir(ruta) #lista los directorios que se encuentran dentro de la carpeta principal
fecha.sort() #ordena el arreglo del año menor al mayor 

i = 0 #para saber en que año va
years = [] #agregar el total del año al arreglo
anual = 0 #contar el total por año
resultados = open("p2.txt", "a")
for f in fecha:
	i+=1
	rutaSecundaria = ruta+f+"/"
	for e in os.listdir(rutaSecundaria):
		archivo = open(rutaSecundaria+e) #abrir el archivo
		cLine = 0 #variable para que no cuente la primera línea, que es la del encabezado de cada archivo
		for line in archivo:
			if(cLine!=0):
				anual+=1 #se incrementa el contador del total de crímenes
			cLine+=1
	if(i%12==0): #si ya se terminó el año 
		resultados.write(str(anual))
		resultados.write('\n')
		years.append(anual) #se agrega el total al arreglo
		anual = 0 #se reinicia el contador de crímenes por año

resultados.close()		
print(years) #imprimir el arreglo de años
print(sum(years)) #sumar las cantidades para comprobar que es igual al resultado de la pregunta 1

ayos = ["2011","2012","2013","2014","2015","2016","2017"]

fig = plt.figure('Crímenes por año')
ax = fig.add_subplot(111)
xx = range(1, len(years)+1)

ax.bar(xx, years, width=0.8,  color=['blue','red','green','orange','brown','purple','pink'], align="center")
ax.set_xticks(xx)
ax.set_xticklabels(ayos)
ax.set_ylabel("Crímenes")

plt.xlabel('Años')
plt.ylabel('Número de crímenes')
plt.show()
