import os
from matplotlib import pyplot as plt
import csv

ruta = "./CrimesUK_2011_2017/"
fecha = os.listdir(ruta) #lista los directorios que se encuentran dentro de la carpeta principal
fecha.sort() #ordena el arreglo de menor a mayor

archivo = open(ruta+"2011-01/2011-01-avon-and-somerset-street.csv")
campos = []
for line in archivo:
	campos = line
	break
archivo.close()
campos2 = []
for i in range(12):
	campos2.append(campos.split(",")[i])
camposF = [0]*12
resultados = open("campos_faltantes.txt", "w")
for f in fecha:
	rutaSecundaria = ruta+f+"/"
	archivos = os.listdir(rutaSecundaria)
	archivos.sort()
	for e in archivos:
		archivo = open(rutaSecundaria+e) #abrir el archivo
		cLine = 0 #variable para que no cuente la primera línea, que es la del encabezado de cada archivo
		for line in archivo:
			if(cLine!=0):
				for r in range(12):
					faltantes = 0
					if(list(csv.reader([line.strip()],delimiter=','))[0][r]==""):
						faltantes+=1
					camposF[r]+=faltantes
			cLine+=1

#sacar porcentajes
totalRegistros = 41286964
for l in range(len(camposF)):
	porcentaje = round(((camposF[l]*100)/totalRegistros),2)
	cadena = str(camposF[l])+"-"+str(porcentaje)
	resultados.write(cadena)
	resultados.write('\n')

#--------------------------------------GRAFICAR-------------------------------------------
#este codigo si muestra la grafica, pero las cantidades las desordena y no hay una distribucion correcta
#se utilizo el archivo txt generado y la grafica se hizo en excel
archivoDatos = open("./campos_faltantes.txt")
i=0
camposPor = [0]*12
for line in archivoDatos:
	camposF[i] = line.split("-")[0]
	camposPor[i] = line.split("-")[1]
	i+=1

fig = plt.figure("Cantidad de datos faltantes por campo")
ax = fig.add_subplot(111)
xx = range(len(camposF))

ax.bar(xx, camposF, color=['blue','red','green','orange','brown','purple','pink','black','gray','yellow','violet','gold'])
ax.set_xticks(xx)
ax.set_xticklabels(campos2, rotation=90)
plt.xlabel("Nombre de los campos")
plt.ylabel('Cantidad de datos faltantes')

rects = ax.patches

for rect, label, i in zip(rects,camposPor,xx):
	ax.text(rect.get_width()+i-1,rect.get_height()+0.2,label+"%",fontsize=10)
    
plt.show()
