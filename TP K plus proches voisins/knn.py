# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 19:04:52 2020

@author: vegret
"""

import csv
import math 
import matplotlib.pyplot as plt

fichier = open("iris.csv",'r')
iris = list(csv.DictReader(fichier))
fichier.close()

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

plt.axis('equal')
plt.scatter(lo_setosa, la_setosa, color='g', label='setosa')
plt.scatter(lo_versicolor, la_versicolor, color='r', label='versicolor')
plt.scatter(lo_virginica, la_virginica, color='b', label='virginica')
plt.scatter(2.5,0.75, color='k')
plt.legend()
plt.show()

def addDistance(la, lo, listepoints):
    for i in range(len(listepoints)):
        distance = math.sqrt((lo - float(listepoints[i]["petal_length"]))**2 + (la - float(listepoints[i]["petal_width"]))**2)
        listepoints[i]["Distance"] = distance

def sortList(tab, critere):
   for i in range(len(tab)):
       min = i
       for j in range(i+1, len(tab)):
           if tab[min][critere] > tab[j][critere]:
               min = j
       tmp = tab[i]
       tab[i] = tab[min]
       tab[min] = tmp
   return tab

def printSpecies(liste, pointsNumber):
    a = []
    for i in range(0, pointsNumber):
        a.append(liste[i]["species"])
    for x in range(len(a)):
        if a[x] == '0':
            a[x] = "setosa"
        elif a[x] == '1':
            a[x] = "versicolor"
        elif a[x] == '2':
            a[x] = "virginica"
    return print("Les", pointsNumber, "iris les plus proches dans l'ordre sont d'especes :", a)

addDistance(0.75, 2.5, iris)

sortList(iris, "Distance")

printSpecies(iris, 3)