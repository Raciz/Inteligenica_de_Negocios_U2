import os
import csv
import collections
from matplotlib import pyplot as plt


#Función para sacer la fecha por separado
def getFecha(fecha):
	fechaSep = list(csv.reader([fecha.strip()],delimiter='-'))[0] #Se separa la fecha
	return int(fechaSep[0]), int(fechaSep[1]), int(list(csv.reader([fechaSep[2].strip()],delimiter='T'))[0][0]) #Se devuelve el año, mes y día

#Función para obtener el día de la semana dada la fecha
def getDiaSemana(fecha):
	anio, mes, dia = getFecha(fecha) #Se obtiene el día, el mes y el año dada la fecha


	#Asignación de la clave del mes
	if mes == 1 or mes == 10:
		mes = 0
	elif mes == 5:
		mes = 1
	elif mes == 8:
		mes = 2
	elif mes == 2 or mes == 3 or mes == 11:
		mes = 3
	elif mes == 6:
		mes = 4
	elif mes==9 or mes==12:
		mes = 5
	elif mes == 4 or mes == 7:
		mes=6

	#Asignación de la clave del siglo
	if (anio>=400 and anio<=499) or (anio>=1100 and anio<=1199) or (anio>=1900 and anio<=1999) or (anio>=2300 and anio<=2399):
		siglo = 0
	elif (anio>=1000 and anio<=1099) or (anio>=300 and anio<=399):
		siglo=1
	elif (anio>=200 and anio<=299) or (anio>=1800 and anio<=1899) or (anio>=2200 and anio<=2299) or (anio>=900 and anio<=999):
		siglo = 2
	elif (anio>=800 and anio<=899) or (anio>=100 and anio<=199):
		siglo = 3
	elif (anio>=1 and anio<=99) or (anio>=1400 and anio<=1499) or (anio>=700 and anio<=799) or (anio>=1700 and anio<=1799) or (anio>=2100 and anio<=2199):
		siglo = 4
	elif (anio>=600 and anio<=699) or (anio>=1300 and anio<=1399):
		siglo = 5
	elif (anio>=1200 and anio<=1299) or (anio>=1600 and anio<=1699) or (anio>=2000 and anio<=2099) or (anio>=500 and anio<=599) or (anio>=2400 and anio<=2499):
		siglo = 6

	#Asignación clave del año
	anio = anio%100

	#Cálculo del día
	res = int((dia + mes + anio + (anio/4) + siglo) % 7)

	#Devolución del día de la semana
	if res == 0 or res == 7:
		return "Domingo"
	elif res == 1:
		return "Lunes"
	elif res == 2:
		return "Martes"
	elif res == 3:
		return "Miércoles"
	elif res == 4:
		return "Jueves"
	elif res == 5:
		return "Viernes"
	elif res == 6:
		return "Sábado"



ruta = "./StopSearch_2011_2017/"
fecha = os.listdir(ruta) #diccionario los directorios que se encuentran dentro de la carpeta principal

#diccionario para guardar el número de los días de la semana encontrados
dias = {
	"Lunes": 0,
	"Martes": 0,
	"Miércoles": 0,
	"Jueves": 0,
	"Viernes": 0,
	"Sábado": 0,
	"Domingo": 0
}


total = 0 #variable que cuenta el total de inspecciones de cada archivo
for f in fecha: #recorre todos los directorios encontrados
	rutaSecundaria = ruta+f+"/" #se prepara la ruta donde se buscarán los archivos
	for e in os.listdir(rutaSecundaria): #se recorren todos los archivos encontrados en ese directorio
		archivo = open(rutaSecundaria+e) #se abre el archivo
		cLine = 0 #variable para que no cuente la primera línea, que es la del encabezado de cada archivo
		for line in archivo:
			if(cLine!=0):
				total+=1 #se incrementa el contador del total de inspecciones
				fecha = list(csv.reader([line.strip()],delimiter=','))[0][1] #separar la linea por comas y asi obtener el registro y guardarlo
				dia = getDiaSemana(fecha) #Se obtiene el día de la semana de esa fecha
				dias[dia] += 1 #Se aumenta el número en el día obtenido

			cLine+=1





#_____________________Generar gráfica_____________________
diasL = [] #Para guardar los días de la semana
porcentajes = [] #Para guardar el porcentaje de cada inspección


print("Total de inspecciones: ",total, "\n") #se imprime el total de inspecciones

#Se generan los resultados
for dia in dias:
	diasL.append(dia)
	porcentajes.append(round(((dias[dia] * 100) / total),2))
	print(diasL[-1], "=", porcentajes[-1])

plt.pie(porcentajes, labels=diasL, colors=None, startangle=90, shadow=None, explode=None, autopct="%1.3f%%")
plt.title("Porcentaje de inspecciones por día de la semana")
plt.show()
