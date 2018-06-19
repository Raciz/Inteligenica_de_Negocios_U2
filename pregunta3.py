import os
from matplotlib import pyplot as plt

ruta = "./CrimesUK_2011_2017/"
fecha = os.listdir(ruta) #lista los directorios que se encuentran dentro de la carpeta principal
fecha.sort() #ordena el arreglo menor a mayor 

months = [] #agregar el total por mes
mesesLabels = []

for f in fecha:
	total = 0 #contar el total por mes
	rutaSecundaria = ruta+f+"/"
	mesesLabels.append(f)
	for e in os.listdir(rutaSecundaria):
		archivo = open(rutaSecundaria+e) #abrir el archivo
		cLine = 0 #variable para que no cuente la primera línea, que es la del encabezado de cada archivo
		for line in archivo:
			if(cLine!=0):
				total+=1 #se incrementa el contador del total de crímenes
			cLine+=1
	months.append(total)
			

		
print(months) #imprimir el arreglo de meses
print(sum(months)) #sumar las cantidades para comprobar que es igual al resultado de la pregunta 1

#pasos para graficar los 84 meses
plt.figure("Crímenes por mes")
num = [y for y in range(1,85)]
plt.plot(num, months, 'g*-');
xx = range(1, len(mesesLabels)+1)
plt.xticks(xx, mesesLabels, rotation=90)
plt.grid(True)
plt.xlabel("Meses")
plt.ylabel("Cantidad de crímenes")
plt.show()
