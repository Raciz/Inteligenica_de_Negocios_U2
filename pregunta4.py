import os
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import spearmanr
import numpy as np
import seaborn as sns

ruta = "./CrimesUK_2011_2017/"
fecha = os.listdir(ruta) #lista los directorios que se encuentran dentro de la carpeta principal
fecha.sort() #ordena el arreglo de menor a mayor

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
			

#agregar las cantidades de cada uno de los 12 meses a su respectivo año
year = [[0] * 12 for i in range(7)]
j=1
p=0
aux = []
for i in range(len(months)):
	aux.append(months[i])
	if(j%12==0):
		year[p] = aux
		aux = []
		p+=1
	j+=1

#Correlación de Spearman 4.2 y mapa de calor 4.3
column_labels = ["2011","2012","2013","2014","2015","2016","2017"]
row_labels = ["2011","2012","2013","2014","2015","2016","2017"]
data = [[None] * 7 for i in range(7)]
for c in range(0,7):
	for o in range(0,7):
		cor, pv = spearmanr(year[c], year[o])
		data[c][o] = cor
		
fig, ax = plt.subplots()
heatmap = ax.pcolor(data, cmap=plt.cm.Reds)

#poner la etiqueta a la mitad del cuadrito
ax.set_xticks(np.arange(len(row_labels))+0.5)
ax.set_yticks(np.arange(len(column_labels))+0.5)

ax.invert_yaxis()
ax.xaxis.tick_top()

ax.set_xticklabels(row_labels, minor=False, size=12)
ax.set_yticklabels(column_labels, minor=False, size=12)

#configuramos la barra de color de referencia del mapa de calor
cb = plt.colorbar(heatmap) 
cb.set_label("Correlación de Spearman por cada pareja de años", size=14)
cb.ax.tick_params(labelsize=12)
fig.tight_layout()

plt.show()

#Scatter Matrix con Scatter Plot 4.4
year2 = [[0] * 7 for i in range(12)]

for j in range(12):
	for l in range(7):
		year2[j][l] = year[l][j]
df = pd.DataFrame(year2, columns=['2011', '2012', '2013', '2014','2015','2016','2017'])
df["Meses"] = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
sns.pairplot(df, kind="scatter", hue="Meses")
plt.show()

#Gráfica de una curva por año 4.1
mesesLabels = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
plt.title("Crímenes por año", size=14)
plt.xlabel("Meses")
plt.ylabel("Cantidad de crímenes")
plt.grid(True)
xx = range(1, len(mesesLabels)+1)
plt.xticks(xx, mesesLabels, rotation=90, size=12)
plt.yticks(size=12)

plt.plot(xx, year[0], '*-')
plt.plot(xx, year[1], '+-')
plt.plot(xx, year[2], 'x-')
plt.plot(xx, year[3], 'd-')
plt.plot(xx, year[4], '1-')
plt.plot(xx, year[5], '2-')
plt.plot(xx, year[6], '3-')

plt.legend(('2011', '2012', '2013','2014','2015','2016','2017'),prop = {'size':12}, loc = 'upper right')

plt.show()
