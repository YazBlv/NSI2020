# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 15:31:11 2020

@author: vegret
"""
billets = [500, 200, 100, 50, 20, 10, 5, 2, 1]

def algoGloutonRendu(prix, donné, listeBillets):
    rendu = []
    totalRendu =  donné - prix
    print('Il faut rendre :', totalRendu)
    if prix <= donné : 
        while not totalRendu == 0:
            for i in range(len(listeBillets)):
                if totalRendu - listeBillets[i] >=0:
                    totalRendu -= listeBillets[i]
                    rendu.append(listeBillets[i])
                    break
    else : 
        print('Il manque de l\'argent')  
        rendu = []          
    return rendu

