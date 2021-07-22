# -*- coding: utf-8 -*-
"""
Created on Thu May 27 21:36:20 2021

@author: juand

EN ESTE CODIGO SE INGRESA UN ESTADO INICIAL DEFINIDO EN activityToday (linea 30) Y UNO FINAL 
EN smaller_list (linea 131) Y LA FUNCIÓN RETORNA LA PROBABILIDAD DE QUE SE DE DICHA TRANSICIÓN DE ESTADOS.

"""
import numpy as np
import random as rm


# Definir los estados 
states = ["ocupado","desocupado","espera","desinfectando"]

# Transición de estados respecto a cada uno 
transitionName = [["OO","OD"],["DO","DD","DE","DDE"],["EE","EDE"],["DEO","DED","DEDE"]]

# Matriz de probabilidad 
transitionMatrix = [[0.66,0.34],[0.2,0.2,0.51,0.09],[0.84,0.16],[0.19,0.19,0.62]]



#Definir el estado inicial
activityToday = "desinfectando"
fin="espera"

def markov(days,activityToday):
  
    activityList = [activityToday]
    i = 0
    prob = 1
    while i != days:
        if activityToday == "ocupado":
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
            if change == "OO":
                prob = prob * 0.66
                activityList.append("ocupado")
                pass
            else:
                prob = prob * 0.34
                activityToday = "desocupado"
                activityList.append("desocupado")
            
                
        elif activityToday == "desocupado":
            change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
            if change == "DD":
                prob = prob * 0.2
                activityList.append("desocupado")
                pass
            elif change == "DO":
                prob = prob * 0.2
                activityToday = "ocupado"
                activityList.append("ocupado")
            elif change == "DE":
                prob = prob * 0.51
                activityToday = "espera"
                activityList.append("espera")
            else:
                prob = prob * 0.09
                activityToday = "desinfectando"
                activityList.append("desinfectando")
                
        elif activityToday == "espera":
            change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
            if change == "EE":
                prob = prob * 0.84
                activityList.append("espera")
                pass
            else:
                prob = prob * 0.16
                activityToday = "desinfectando"
                activityList.append("desinfectando")
                
                
        elif activityToday == "desinfectando":
            change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
            if change == "DEDE":
                prob = prob * 0.62
                activityList.append("desinfectando")
                pass
            elif change == "DEO":
                prob = prob * 0.19
                activityToday = "ocupado"
                activityList.append("ocupado")
                
            else:
                prob = prob * 0.19
                activityToday = "desocupado"
                activityList.append("desocupado")
                
                
                
        i += 1  
    return activityList
   

list_activity = []
count = 0

# realizar 10000 iteraciones respecto a las que se ponen cuando se llama la función
for iterations in range(1,10000):
        list_activity.append(markov(10,activityToday))




for smaller_list in list_activity:
    if(smaller_list[2] == fin): #Seleccionar el estado final 
        count += 1

# Calcular la probabilidad de iniciar en el estado (ActivityToday) y terminar en el establecido en smaller_list
percentage = (count/10000) * 100
print("La probabilidad de iniciar en el estado: " + activityToday + " y Terminar en el estado: "+  fin + " = " + str(percentage) + "%")
