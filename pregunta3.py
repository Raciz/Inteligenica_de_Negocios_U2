import os
from matplotlib import pyplot as plt
#import csv
#print(list(csv.reader([line.strip()],delimiter=','))[0]) #separar la linea por comas y asi obtener los registros

ruta = "./CrimesUK_2011_2017/"
fecha = os.listdir(ruta) #lista los directorios que se encuentran dentro de la carpeta principal
fecha.sort() #ordena el arreglo del año menor al mayor 

months = [] #agregar el total del año al arreglo
mesesLabels = []

for f in fecha:
	total = 0 #contar el total por año
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
			

		
print(months) #imprimir el arreglo de años
print(sum(months)) #sumar las cantidades para comprobar que es igual al resultado de la pregunta 1

plt.figure("Crímenes por mes")
num = [y for y in range(1,85)]
plt.plot(num, months, 'g*-');
xx = range(1, len(mesesLabels)+1)
plt.xticks(xx, mesesLabels, rotation=90)
plt.grid(True)
plt.xlabel("Meses")
plt.ylabel("Cantidad de crímenes")
plt.show()

"""fig = plt.figure('Crímenes por mes', figsize=(5,100))
ax = fig.add_subplot(111)
xx = range(1, len(mesesLabels)+1)

ax.barh(xx, months, color=['blue','red','green','orange','brown','purple','pink','cyan','yellow','gray','gold','black'], align="center",  edgecolor='none')
ax.set_yticks(xx)
ax.set_yticklabels(mesesLabels)

plt.xlabel('Cantidad de crímenes')
plt.ylabel('Meses')
plt.show()"""
