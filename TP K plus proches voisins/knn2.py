# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 19:04:52 2020

@author: Francois
"""

import csv
import matplotlib.pyplot as plt
import math
fichier = open("iris.csv",'r')
iris = list(csv.DictReader(fichier))
fichier.close()

def calculdistance(x0,y0,x1,y1):
    return math.sqrt((x1-x0)**(2)+(y1-y0)**(2))
          
def triliste(liste,criteretri):
    for i in range(len(liste)):
        index_mini = i
        for j in range(i+1,len(liste)):
            if liste[j][criteretri] < liste[index_mini][criteretri]:
                index_mini = j
        tmp = liste[i]
        liste[i]=liste[index_mini]
        liste[index_mini]=tmp
        
def rechercheknn(liste,k,info,categorie):
    knn = []
    for i in range(0,k):
        knn.append(liste[i][info])
    maxi =0
    for cat in categorie:
        num = knn.count(cat)
        if num>maxi:
            maxi = num
            bonneCategorie = cat
    return bonneCategorie
    
        

lo_setosa = []
la_setosa = []
lo_versicolor = []
la_versicolor = []
lo_virginica = []
la_virginica = []

for i in range(len(iris)):
    if iris[i]["species"]=="0":
        lo_setosa.append(float(iris[i]["petal_length"]))
        la_setosa.append(float(iris[i]["petal_width"]))
    elif iris[i]["species"]=="1":
        lo_versicolor.append(float(iris[i]["petal_length"]))
        la_versicolor.append(float(iris[i]["petal_width"]))
    elif iris[i]["species"]=="2":
        lo_virginica.append(float(iris[i]["petal_length"]))
        la_virginica.append(float(iris[i]["petal_width"]))

for i in range(len(iris)):
    iris[i]["dist"]=calculdistance(float(iris[i]["petal_length"]),float(iris[i]["petal_width"]),2.5,0.75)

triliste(iris,"dist")

trouve_iris = int(rechercheknn(iris,3,"species",["0","1","2"]))
espese=["setosa","versicolor","virginica"]
print(espese[trouve_iris])


plt.axis('equal')
plt.scatter(lo_setosa, la_setosa, color='g', label='setosa')
plt.scatter(lo_versicolor, la_versicolor, color='r', label='versicolor')
plt.scatter(lo_virginica, la_virginica, color='b', label='virginica')
plt.scatter(2.5,0.75, color='k')
plt.legend()
plt.show()