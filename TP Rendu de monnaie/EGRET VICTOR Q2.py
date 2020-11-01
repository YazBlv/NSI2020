# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 15:31:11 2020

@author: vegret
"""
#Import de la librairie d'interface graphique
import tkinter as tk
from tkinter import font as tkFont

#Liste des types de billets disponibles
billets = [500, 200, 100, 50, 20, 10, 5, 2, 1]

prixTotal = ""
donné = ""
currentVal = "Prix"

#Fonction de rendu de monnaie
def algoGloutonRendu(prix, donné, listeBillets):
    rendu = []
    totalRendu = donné - prix
    if prix <= donné : 
        totalRenduSave = totalRendu
        while not totalRendu == 0:
            for i in range(len(listeBillets)):
                if totalRendu - listeBillets[i] >=0:
                    totalRendu -= listeBillets[i]
                    rendu.append(listeBillets[i])
                    break  
        arendreTexte.set("Rendre : " + str(totalRenduSave) + "€ " + str(rendu))         
    else : 
        arendreTexte.set("Il manque de l\'argent")  
        rendu = []   
    return rendu

fenetre = tk.Tk()
fenetre.title("Caisse enregistreuse")
fenetre.geometry("800x500")

Font25 = tkFont.Font(family="Arial", size=25)
Font18 = tkFont.Font(family="Arial", size=18)

prixTexte = tk.StringVar()
prixTexte.set("Prix : 0€")
prixlabel = tk.Label(fenetre,textvar=prixTexte, font=Font18)
prixlabel.pack()

clientTexte = tk.StringVar()
clientTexte.set("Client : 0€")
client = tk.Label(fenetre,textvar=clientTexte, font=Font18)
client.pack()

arendreTexte = tk.StringVar()
arendreTexte.set("Rendre : ")
arendre = tk.Label(fenetre,textvar=arendreTexte, font=Font18)
arendre.pack()

#Fonction qui change la valeur en cours d'édition
def changeCurrentVal():
    global currentVal
    if currentVal == "Prix":
        currentVal = "Client"
    elif currentVal == "Client":
        currentVal = "Prix"
    changevalTexte.set("Édition de : " + currentVal)    
        
#Fonction des bouttons pour changer/remettre a 0 le prix ou ce que le client a donné
def changeVal(val, number, reset):
    global prixTotal
    global donné
    if val == "Prix":
        if reset == True:
            prixTotal = ""
            prixTexte.set("Prix : 0€")
        else:    
            if number == "0":
                prixTotal = str(int(prixTotal) * 10)
            else:  
                prixTotal += number
            prixTexte.set("Prix : " + prixTotal + "€")
    elif val == "Client":
        if reset == True:
            donné = ""
            clientTexte.set("Client : 0€")
        else:    
            if number == "0":
                donné = str(int(donné) * 10)
            else:  
                donné += number
            clientTexte.set("Client : " + donné + "€")

#Bouttons de saisie 
button1 = tk.Button(fenetre,text="1",font=Font25,command= lambda : changeVal(currentVal, "1", False))
button1.place(width=75, height=75,x=275,y=100)
button2 = tk.Button(fenetre,text="2",font=Font25,command= lambda : changeVal(currentVal, "2", False))
button2.place(width=75, height=75,x=350,y=100)
button3 = tk.Button(fenetre,text="3",font=Font25,command= lambda : changeVal(currentVal, "3", False))
button3.place(width=75, height=75,x=425,y=100)
button4 = tk.Button(fenetre,text="4",font=Font25,command= lambda : changeVal(currentVal, "4", False))
button4.place(width=75, height=75,x=275,y=175)
button5 = tk.Button(fenetre,text="5",font=Font25,command= lambda : changeVal(currentVal, "5", False))
button5.place(width=75, height=75,x=350,y=175)
button6 = tk.Button(fenetre,text="6",font=Font25,command= lambda : changeVal(currentVal, "6", False))
button6.place(width=75, height=75,x=425,y=175)
button7 = tk.Button(fenetre,text="7",font=Font25,command= lambda : changeVal(currentVal, "7", False))
button7.place(width=75, height=75,x=275,y=250)
button8 = tk.Button(fenetre,text="8",font=Font25,command= lambda : changeVal(currentVal, "8", False))
button8.place(width=75, height=75,x=350,y=250)
button9 = tk.Button(fenetre,text="9",font=Font25,command= lambda : changeVal(currentVal, "9", False))
button9.place(width=75, height=75,x=425,y=250)
button0 = tk.Button(fenetre,text="0",font=Font25,command= lambda : changeVal(currentVal, "0", False))
button0.place(width=75, height=75,x=350,y=325)

#Boutton pour arreter le programme et fermer la fenetre
quitbutton = tk.Button(fenetre,text="Quitter",bg="red",fg="white",font=Font18,command= lambda : fenetre.destroy())
quitbutton.place(width=75, height=75,x=100,y=175)

#Boutton de remise à 0 du prix
razbutton = tk.Button(fenetre,text="RAZ",font=Font25,command= lambda : changeVal(currentVal, "0", True))
razbutton.place(width=75, height=75,x=275,y=325)

#Boutton de calcul du rendu
equalbutton = tk.Button(fenetre,text="=",font=Font25,command= lambda : algoGloutonRendu(int(prixTotal), int(donné), billets))
equalbutton.place(width=75, height=75,x=425,y=325)

changevalTexte = tk.StringVar()
changevalTexte.set("Édition de : " + currentVal)

#Boutton pour changer la valeur en cours d'édition (le prix ou ce que le client a donné)
changevalbutton = tk.Button(fenetre,textvar=changevalTexte,font=Font25,command= lambda : changeCurrentVal())
changevalbutton.place(width=300, height=75,x=240,y=405)

fenetre.mainloop()
