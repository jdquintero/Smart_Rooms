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
transitionName = [["OO","OD","OE","OD"],["DO","DD","DE","DDE"],["EO","ED","EE","EDE"],["DEO","DED","DEE","DEDE"]]

# Matriz de probabilidad 
transitionMatrix = [[0.5,0.5,0,0],[0,0.6,0.4,0],[0.3,0.3,0.1,0.3],[0.4,0.4,0,0.2]]


#Definir el estado inicial
activityToday = "desocupado"

def markov(days,activityToday):
  
    activityList = [activityToday]
    i = 0
    prob = 1
    while i != days:
        if activityToday == "ocupado":
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
            if change == "OO":
                prob = prob * 0.5
                activityList.append("ocupado")
                pass
            elif change == "OD":
                prob = prob * 0.5
                activityToday = "desocupado"
                activityList.append("desocupado")
            elif change == "OE":
                prob = prob * 0
                activityToday = "espera"
                activityList.append("espera")
            else:
                prob = prob * 0
                activityToday = "desinfectando"
                activityList.append("desinfectando")
                
        elif activityToday == "desocupado":
            change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
            if change == "DD":
                prob = prob * 0.6
                activityList.append("desocupado")
                pass
            elif change == "DO":
                prob = prob * 0
                activityToday = "ocupado"
                activityList.append("ocupado")
            elif change == "DE":
                prob = prob * 0.4
                activityToday = "espera"
                activityList.append("espera")
            else:
                prob = prob * 0
                activityToday = "espera"
                activityList.append("espera")
                
        elif activityToday == "espera":
            change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
            if change == "EE":
                prob = prob * 0.1
                activityList.append("espera")
                pass
            elif change == "EO":
                prob = prob * 0.3
                activityToday = "ocupado"
                activityList.append("ocupado")
            elif change == "ED":
                prob = prob * 0.3
                activityToday = "desocupado"
                activityList.append("desocupado")
            else:
                prob = prob * 0.3
                activityToday = "desinfectando"
                activityList.append("desinfectando")
                
                
        elif activityToday == "desinfectando":
            change = np.random.choice(transitionName[3],replace=True,p=transitionMatrix[2])
            if change == "DEDE":
                prob = prob * 0.2
                activityList.append("desinfectando")
                pass
            elif change == "DEO":
                prob = prob * 0.4
                activityToday = "ocupado"
                activityList.append("ocupado")
            elif change == "DED":
                prob = prob * 0.4
                activityToday = "desocupado"
                activityList.append("desocupado")
            else:
                prob = prob * 0
                activityToday = "desinfectando"
                activityList.append("desinfectando")
                
                
                
        i += 1  
    return activityList
   

list_activity = []
count = 0

# realizar 10000 iteraciones respecto a las que se ponen cuando se llama la función
for iterations in range(1,10000):
        list_activity.append(markov(10,activityToday))



for smaller_list in list_activity:
    if(smaller_list[2] == "desinfectando"): #Seleccionar el estado final 
        count += 1

# Calcular la probabilidad de iniciar en el estado (ActivityToday) y terminar en el establecido en smaller_list
percentage = (count/10000) * 100
print("La probabilidad de iniciar en el estado: " + activityToday + "  y Terminar en el estado: desinfectando = " + str(percentage) + "%")