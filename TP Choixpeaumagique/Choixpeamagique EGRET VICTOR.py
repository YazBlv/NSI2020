# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 13:24:51 2020

@author: Greentor
"""

import csv
import math 
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import font as tkFont

def loadFile(fileName):
    """
    Copie le fichier puis le renvoie 
    sous forme de dictionnaire
    
    Parameters
    ----------
    fileName : string
        Nom du fichier csv 

    Returns
    -------
    liste : OrderedDict
        Liste du contenu du fichier csv
    """
    
    fichier = open(fileName,'r', encoding='utf-8')
    liste = list(csv.DictReader(fichier))
    fichier.close()
    return liste

def getDistance(eleve1, eleve2):
    """
    Compare les données des eleves puis
    renvoie la distance 
    
    Parameters
    ----------
    eleve1 : OrderedDict
        Premier eleve 
        
    eleve2 : OrderedDict
        Deuxieme eleve

    Returns
    -------
    distance : float
        Distance entre les deux eleves
    """

    Courage = (int(eleve2['Courage']) - int(eleve1['Courage']))**2
    Loyauté = (int(eleve2['Loyauté']) - int(eleve1['Loyauté']))**2
    Sagesse = (int(eleve2['Sagesse']) - int(eleve1['Sagesse']))**2
    Malice = (int(eleve2['Malice']) - int(eleve1['Malice']))**2

    distance = math.sqrt(Courage + Loyauté + Sagesse + Malice)

    return distance

def addDistance(eleveList, eleve):
    """
    Compare les données des eleves puis
    renvoie la distance 
    
    Parameters
    ----------
    eleveList : List
        Liste des eleves
        
    eleve : OrderedDict
        Deuxieme eleve

    Returns
    -------
    eleveList : List
        Liste des eleves avec la distance au parametre eleve pour chaque eleve
    """

    for x in range(len(eleveList)):
        eleveList[x]['Distance'] = getDistance(eleveList[x], eleve)

    return eleveList

def sortList(tab, critere):
    """
    Trie la liste en fonction du critere donné
    
    Parameters
    ----------
    tab : List
        Liste à trier
        
    critere : str
        Critere de tri

    Returns
    -------
    tab : List
        Liste triée
    """

    for i in range(len(tab)):
        min = i
        for j in range(i+1, len(tab)):
            if tab[min][critere] > tab[j][critere]:
                min = j
        tmp = tab[i]
        tab[i] = tab[min]
        tab[min] = tmp
    return tab

def getAffectation(eleveList):
    """
    Donne l'affectation de la liste donnée
    
    Parameters
    ----------
    eleveList : List
        Liste d'eleves

    Returns
    -------
    affectation : str
        Maison d'affectation
    """

    #a est la liste contenant les maisons des 10 eleves les plus proches
    a = []
    sortedList = sortList(eleveList, 'Distance')

    maisons = ['Serpentar', 'Serdaigle', 'Poufsouffle', 'Griffondor']

    for i in range(0, 11):
        a.append(sortedList[i]['Maison'])

    maxi =0
    for ma in maisons:
        num = a.count(ma)
        if num>maxi:
            maxi = num
            affectation = ma
    return affectation

fenetre = tk.Tk()
fenetre.title("Choixpeaumagique")
fenetre.geometry("800x500")

Font18 = tkFont.Font(family="Arial", size=18)

x = 125

courage = tk.Label(fenetre,text="Courage",font=Font18)
courage.place(x=x,y=125)
courageEntry = tk.Entry(fenetre, bd =5)
courageEntry.place(x=x+140,y=125)

loyaute = tk.Label(fenetre,text="Loyauté",font=Font18)
loyaute.place(x=x,y=185)
loyauteEntry = tk.Entry(fenetre, bd =5)
loyauteEntry.place(x=x+140,y=185)

sagesse = tk.Label(fenetre,text="Sagesse",font=Font18)
sagesse.place(x=x,y=245)
sagesseEntry = tk.Entry(fenetre, bd =5)
sagesseEntry.place(x=x+140,y=245)

malice = tk.Label(fenetre,text="Malice",font=Font18)
malice.place(x=x,y=305)
maliceEntry = tk.Entry(fenetre, bd =5)
maliceEntry.place(x=x+140,y=305)

affectationTexte = tk.StringVar()
affectationTexte.set("Affectation : ")
affectationlabel = tk.Label(fenetre,textvar=affectationTexte, font=Font18)
affectationlabel.place(x=575,y=150)

affectButton = tk.Button(fenetre,text="Affecter",font=Font18,command= lambda : affectationTexte.set("Affectation :\n" + getAffectation(addDistance(loadFile("choixpeauMagique.csv"), {'Courage': courageEntry.get(), 'Loyauté': loyauteEntry.get(), 'Sagesse': sagesseEntry.get(), 'Malice': maliceEntry.get()}))))
affectButton.place(width=95, height=30,x=425,y=215)

fenetre.mainloop()
