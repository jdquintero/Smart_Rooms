# -*- coding: utf-8 -*-
"""
Created on Thu May 27 21:36:20 2021

@author: juand

ESTE CODIGO SE ESCOGE UN ESTADO INICIAL Y DEVUELVE LOS POSIBLES ESTADOS DESPUES DE LAS ITERACIONES
ESTABLECIDAS Y EL ESTADO FINAL DESPUÉS DE ESTA DADA CON SU PROBABILIDAD.
"""

import numpy as np
import random as rm



# Definir los estados 
states = ["ocupado","desocupado","espera","desinfectando"]

# Transición de estados respecto a cada uno 
transitionName = [["OO","OD"],["DO","DD","DE","DDE"],["EE","EDE"],["DEO","DED","DEDE"]]

# Matriz de probabilidad 
transitionMatrix = [[0.66,0.34],[0.2,0.2,0.51,0.09],[0.84,0.16],[0.19,0.19,0.62]]





def markov(iteraciones):
    # Escoger el estado inicial 
    activityToday = "desinfectando"
    print("Estado Inicial: " + activityToday)
    activityList = [activityToday]
    i = 0

    prob = 1
    while i != iteraciones:
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
    print("Posibles estados: " + str(activityList))
    print("Estado final despues de  "+ str(iteraciones) + " iteraciones: " + activityToday)
    print("Probabilidad de la posible secuencia de estados: " + str(prob))

# Llamar la función con el numero de iteraciones que se desea que haga el codigo.
markov(10)  
