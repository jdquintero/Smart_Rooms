# -*- coding: utf-8 -*-
"""
Created on Thu May 27 18:51:25 2021

@author: juand
"""
import random
import numpy as np
salones=[]
cont=0;

"Ingresar las variables de control"
max_personas=15;
max_tiempo= 30; #menos de 30 min=1,entre 30-60 = 0.5, mas de 60 =0.25"
max_nivel= 700; #en un aula, los niveles normales de dióxido de carbono deben estar "
                #"entre los 500 ppm y los 700 ppm"
max_hora= 60; #"mas de una hora =1, de 30-60min= 0.5, menos de 30min= 0.25"
max_alerta= 10; #"10 alertas por el no uso de tapabocas ""



def prioridad(sal):
    global cont
    while cont < sal:
        cont= cont+1
        "valores aleatorias para cada variable del salón"
        personas =  random.randint(1,30);
        tiempo =   random.randint(1,300);
        nivel =  random.randint(300,2000);
        hora =  random.randint(1,300);
        alerta =  random.randint(0,50);
        
        personas = float(personas)
        tiempo =   float(tiempo)
        nivel =  float(nivel)
        hora = float(hora)
        alerta =  float(alerta)
        
        puntaje= float(0);
        
        
        
        puntaje= float(0);
        
        valor=float(0)
        # personas 
        valor= (personas*100/max_personas)/100;
        puntaje= puntaje +  valor
        valor=0;
        
        #Tiempo siguiente clase
        valor= (tiempo*100/max_tiempo)/100;
        if valor<1:
            valor= valor+1
            if tiempo <= (max_tiempo/2):
                valor= valor+1  
           
        
        
        if tiempo>max_tiempo :
           valor = valor * 0.1
        
        puntaje= puntaje + valor 
        valor=0;
        
        #Nivel Co2
        valor= (nivel*100/max_nivel)/100;
        puntaje= puntaje + valor;
        valor=0;
        
        #Hora ultima desinfección
        valor= (hora*100/max_hora)/100;
        puntaje= puntaje +  valor;
        valor=0;
        
        # Alertas
        valor= (hora*100/max_hora)/100;
        puntaje= puntaje +  valor;
        valor=0;
            
        salones.append(puntaje)
     
           
    #Acá sale del while
    return salones

prioridad(20)
        
salones_org= sorted(salones,reverse=True)
a=salones_org[0]
b=salones_org[1]
c=salones_org[2]

print("Primer salon a desinfectar: ",salones.index(a) )
print("Segundo salon a desinfectar: ",salones.index(b) )
print("Tercer salon a desinfectar: ",salones.index(c) )