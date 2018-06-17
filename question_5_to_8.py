
get_ipython().magic(u'matplotlib inline')
import sys, os
import pandas as pd
import matplotlib.pyplot as plot
import numpy as np



#lista con el nombre de las fuerza policiacas
forces = os.listdir("./CrimesUK_2011_2017/2011-01")

#borramos lo necesario para quedarnos solo con el nombre de la fuerza
for i in range(len(forces)):
    forces[i] = forces[i][8:-11]

#lista con el nombre de todos los crimenes
crimes =['Burglary','Public order','Shoplifting','Drugs','Public disorder and weapons','Other crime','Anti-social behaviour','Other theft','Bicycle theft','Violent crime','Robbery','Vehicle crime','Violence and sexual offences','Criminal damage and arson','Theft from the person','Possession of weapons']

#lista para sumar los crimenes reportados por cada fuerza
forcesCrimes = [0] * len(forces)

#lista para sumar cuantas veces se reporto cada crimen
typesCrimes = [0] * len(crimes)

#lista para sumar los crimenes reportados de cada fuerza policiaca por cada tipo de crimen 
forcesTypeCrimes = [0] * len(forces)
for i in range(len(forces)):
    forcesTypeCrimes[i] = [0] * len(crimes) 
    
#lista para sumar los crimenes reportados de cada tipo de crimen por cada mes
monthTypeCrimes = [0] * len(crimes)
for i in range(len(crimes)):
    monthTypeCrimes[i] = [0] * 12
    
totalCrimes = 0.0



for i in ["2011-","2012-","2013-","2014-","2015-","2016-","2017-"]:
    for j in ["01","02","03","04","05","06","07","08","09","10","11","12"]:
        for k in range(len(forces)):
            
            #abrimos el archivo mediantes pandas para obtener un dataframe
            dataset = pd.read_csv("./CrimesUK_2011_2017/"+i+j+"/"+i+j+"-"+forces[k]+"-street.csv", header=0)
            
            totalCrimes += len(dataset)
            
            #contamos el numero de filas del dataFrame y lo sumamos a la fuerza policiaca correspondiente
            forcesCrimes[k] += len(dataset)

            for l in range(len(crimes)):
                typesCrimes[l] += len(dataset[dataset["Crime type"] == crimes[l]]) 
                
                forcesTypeCrimes[k][l] += len(dataset[dataset["Crime type"] == crimes[l]])
                
                month = (int)(j)
                monthTypeCrimes[l][month-1] += len(dataset[dataset["Crime type"] == crimes[l]])




fig = plot.figure(figsize=(11,18))
ax = fig.add_subplot(111)

numBar = range(len(forces))

ax.barh(numBar, forcesCrimes, color=["red","yellow","blue","brown","gray","orange","white"], edgecolor=["black"] * len(forces) , height=0.8,align="center")
ax.set_yticks(numBar)
ax.set_yticklabels(forces,fontsize=15,fontweight="bold")

plot.ylabel("Fuerza Policiaca",fontsize=15,fontweight="bold")
plot.xlabel("Numero de Crimenes",fontsize=15,fontweight="bold")
plot.title("Pregunta 5: Cuantos y que porcentaje de los crimenes reportados entre 2011 y 2017 corresponden a cada fuerza policiaca",fontsize=15,fontweight="bold")

rects = ax.patches
labels = []
    
for i in forcesCrimes:
    labels.append((str)(i/totalCrimes))
    
for rect, label, i in zip(rects,labels,numBar):    
    ax.text(rect.get_width() + 100000,i-0.2,label+" %",fontsize=15,fontweight="bold")
    
plot.show()

