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



def prioridad():
    global cont
    while cont < 5:
        cont= cont+1
        "valores aleatorias para cada variable del salón"
        personas =  random.randint(1,30)
        tiempo =   random.randint(1,300)
        nivel =  random.randint(300,2000)
        hora =  random.randint(1,300)
        alerta =  random.randint(0,50)
        
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
   
    
   
# prioridad(5)
        
# salones_org= sorted(salones,reverse=True)
# a=salones_org[0]
# b=salones_org[1]
# c=salones_org[2]

# # print("Primer salon a desinfectar: ",salones.index(a) )
# # print("Segundo salon a desinfectar: ",salones.index(b) )
# # print("Tercer salon a desinfectar: ",salones.index(c) )

# salon_1=salones[0]
# salon_2=salones[1]
# salon_3=salones[2]
# salon_4=salones[3]
# salon_5=salones[4]

#determinar probabilidad transición

#DEFINIR ESTADOS INICIALES DE LOS 5 SALONES

estados=["ocupado","desocupado","espera","desinfectando"]
estados1=["ocupado","desocupado"]


salon1=estados[random.randint(0,3)]
salon2=estados[random.randint(0,3)]
salon3=estados[random.randint(0,3)]
salon4=estados[random.randint(0,3)]
salon5=estados[random.randint(0,3)]




#VERIFICAR QUE NO HAYAN DOS SALONES EN ESTADO DESINFECTANDO AL MISMO TIEMPO.
if salon1=="desinfectando":  
    if salon2=="desinfectando":
        salon2=estados[random.randint(0,2)]
    if salon3=="desinfectando":
        salon3=estados[random.randint(0,2)]
    if salon4=="desinfectando":
        salon4=estados[random.randint(0,2)]
    if salon5=="desinfectando":
        salon5=estados[random.randint(0,2)]
        
if salon2=="desinfectando":  
    if salon3=="desinfectando":
        salon3=estados[random.randint(0,2)]
    if salon4=="desinfectando":
        salon4=estados[random.randint(0,2)]
    if salon5=="desinfectando":
        salon5=estados[random.randint(0,2)]
        
if salon3=="desinfectando":  
    if salon4=="desinfectando":
        salon4=estados[random.randint(0,2)]
    if salon5=="desinfectando":
        salon5=estados[random.randint(0,2)]

if salon4=="desinfectando":  
    if salon5=="desinfectando":
        salon5=estados[random.randint(0,2)]




print(salon1)
print(salon2)
print(salon3)
print(salon4)
print(salon5)
#_______
ocupado_1=0
desocupado_1=0
desinfectando_1=0
espera_1=0

ocupado_2=0
desocupado_2=0
desinfectando_2=0
espera_2=0

ocupado_3=0
desocupado_3=0
desinfectando_3=0
espera_3=0

ocupado_4=0
desocupado_4=0
desinfectando_4=0
espera_4=0

ocupado_5=0
desocupado_5=0
desinfectando_5=0
espera_5=0
#___________________________________
ocupado_desocupado1=0
desocupado_desinfectando1=0
desinfectando_desocupado1=0
desocupado_ocupado1=0
desocupado_espera1=0
espera_desinfectando1=0
desinfectando_ocupado1=0

ocupado_desocupado2=0
desocupado_desinfectando2=0
desinfectando_desocupado2=0
desocupado_ocupado2=0
desocupado_espera2=0
espera_desinfectando2=0
desinfectando_ocupado2=0


ocupado_desocupado3=0
desocupado_desinfectando3=0
desinfectando_desocupado3=0
desocupado_ocupado3=0
desocupado_espera3=0
espera_desinfectando3=0
desinfectando_ocupado3=0


ocupado_desocupado4=0
desocupado_desinfectando4=0
desinfectando_desocupado4=0
desocupado_ocupado4=0
desocupado_espera4=0
espera_desinfectando4=0
desinfectando_ocupado4=0


ocupado_desocupado5=0
desocupado_desinfectando5=0
desinfectando_desocupado5=0
desocupado_ocupado5=0
desocupado_espera5=0
espera_desinfectando5=0
desinfectando_ocupado5=0



contador_espera1=0
contador_espera2=0
contador_espera3=0
contador_espera4=0
contador_espera5=0

lista=[]

bandera_libre=0

#________________________________
iteraciones=10000; #INGRESAR EL NUMERO DE ITERACIONES PARA OBTENER LA TRANSICION DE ESTADOS
contador_iteraciones=0;

while contador_iteraciones<iteraciones:
    contador_iteraciones=contador_iteraciones+1;
    prioridad()
    #print(salones)
    
        
    salones_org= sorted(salones,reverse=True)
    a=salones_org[0]
    b=salones_org[1]
    c=salones_org[2]
    
    # print("Primer salon a desinfectar: ",salones.index(a) )
    # print("Segundo salon a desinfectar: ",salones.index(b) )
    # print("Tercer salon a desinfectar: ",salones.index(c) )
    
    salon_1=salones[0]
    salon_2=salones[1]
    salon_3=salones[2]
    salon_4=salones[3]
    salon_5=salones[4]
    
    
#SI EL ESTADO INCIAL ES OCUPADO

    if salon1== "ocupado" :
        ocupado_1=ocupado_1+1
        salon1=estados[random.randint(0,1)]
        if salon1=="desocupado":
            ocupado_desocupado1=ocupado_desocupado1+1
        
    if salon2== "ocupado" :
        ocupado_2=ocupado_2+1
        salon2=estados[random.randint(0,1)]
        if salon2=="desocupado":
            ocupado_desocupado2=ocupado_desocupado2+1
        
    if salon3== "ocupado" :
        ocupado_3=ocupado_3+1
        salon3=estados[random.randint(0,1)]
        if salon3=="desocupado":
            ocupado_desocupado3=ocupado_desocupado3+1
        
    if salon4== "ocupado" :
        ocupado_4=ocupado_4+1
        salon4=estados[random.randint(0,1)]
        if salon4=="desocupado":
            ocupado_desocupado4=ocupado_desocupado4+1
        
    if salon5== "ocupado" :
        ocupado_5=ocupado_5+1
        salon5=estados[random.randint(0,1)]
        if salon5=="desocupado":
            ocupado_desocupado5=ocupado_desocupado5+1
 
#SI EL ESTADO INICIAL ES DESOCUPADO

#SALON1________________________DESOCUPADO________________________________________________
    if salon1 == "desocupado":
        
        if salon_1 == salones_org[0]: #Si el salon llega a tener prioridad alta
            if salon2 == "desinfectando" or salon3 == "desinfectando" or salon4 == "desinfectando" or salon5 == "desinfectando":
                bandera_alta1=1;
                salon1="espera"
                desocupado_espera1=desocupado_espera1+1
                
                if "salon1" in lista: 
                    aaa=1
                else:
                    lista.append("salon1")  
            else:
                salon1="desinfectando"
                desocupado_desinfectando1=desocupado_desinfectando1+1
                    
        if salon_1==salones_org[1] or salon_1==salones_org[2]:
            salon1="espera"
            contador_espera1=contador_espera1+1
            desocupado_espera1=desocupado_espera1+1
            if "salon1" in lista: 
                aaa=1      
            else:
                lista.append("salon1")
            
        if salon_1 != salones_org[0] and salon_1 != salones_org[1] and salon_1 != salones_org[2]:
            salon1=estados[random.randint(0,1)]
            if salon1=="desocupado":
                desocupado_1=desocupado_1+1
            else:
                desocupado_ocupado1=desocupado_ocupado1+1
                
#___________________________________________________________________________________________________________     

#SALON2________________________________DESOCUPADO___________________________________________      
    if salon2 == "desocupado":
        if salon_2 == salones_org[0]: #Si el salon llega a tener prioridad alta
            if salon1 == "desinfectando" or salon3 == "desinfectando" or salon4 == "desinfectando" or salon5 == "desinfectando":
                bandera_alta2=1;
                salon2="espera"
                desocupado_espera2=desocupado_espera2+1
                if "salon2" in lista: 
                    aaa=1
                    
                else:
                    lista.append("salon2")
            else:
                salon2="desinfectando"
                desocupado_desinfectando2=desocupado_desinfectando2+1
                    
        if salon_2==salones_org[1] or salon_2==salones_org[2]:
            salon2="espera"
            contador_espera2=contador_espera2+1
            desocupado_espera2=desocupado_espera2+1
            if "salon2" in lista: 
                    aaa=1    
            else:
                lista.append("salon2")
            
        if salon_2 != salones_org[0] and salon_2 != salones_org[1] and salon_2 != salones_org[2]:
            salon2=estados[random.randint(0,1)]
            if salon2=="desocupado":
                desocupado_2=desocupado_2+1
            else:
                desocupado_ocupado2=desocupado_ocupado2+1
#__________________________________________________________________________________________________


#SALON3________________________________DESOCUPADO___________________________________________      
    if salon3 == "desocupado":
        if salon_3 == salones_org[0]: #Si el salon llega a tener prioridad alta
            if salon1 == "desinfectando" or salon2 == "desinfectando" or salon4 == "desinfectando" or salon5 == "desinfectando":
                bandera_alta3=1;
                salon3="espera"
                desocupado_espera3=desocupado_espera3+1
                if "salon3" in lista: 
                    aaa=1
                
                else:
                    lista.append("salon3")
            else:
                salon3="desinfectando"
                desocupado_desinfectando3=desocupado_desinfectando3+1
                    
        if salon_3==salones_org[1] or salon_3==salones_org[2]:
            salon3="espera"
            contador_espera3=contador_espera3+1
            desocupado_espera3=desocupado_espera3+1
            if "salon3" in lista: 
                    aaa=1
                
            else:
                lista.append("salon3")
            
        if salon_3 != salones_org[0] and salon_3 != salones_org[1] and salon_3 != salones_org[2]:
            salon3=estados[random.randint(0,1)]
            if salon3=="desocupado":
                desocupado_3=desocupado_3+1
            else:
                desocupado_ocupado3=desocupado_ocupado3+1
#__________________________________________________________________________________________________
 
#SALON4________________________________DESOCUPADO___________________________________________      
    if salon4 == "desocupado":
        if salon_4 == salones_org[0]: #Si el salon llega a tener prioridad alta
            if salon1 == "desinfectando" or salon2 == "desinfectando" or salon3 == "desinfectando" or salon5 == "desinfectando":
                bandera_alta4=1;
                salon4="espera"
                desocupado_espera4=desocupado_espera4+1
                if "salon4" in lista: 
                    aaa=1
                else:
                    lista.append("salon4")
            else:
                salon4="desinfectando"
                desocupado_desinfectando4=desocupado_desinfectando4+1
                    
        if salon_4==salones_org[1] or salon_4==salones_org[2]:
            salon4="espera"
            contador_espera4=contador_espera4+1
            desocupado_espera4=desocupado_espera4+1
            if "salon4" in lista: 
                aaa=1
            else:
                lista.append("salon4")
            
        if salon_4 != salones_org[0] and salon_4 != salones_org[1] and salon_4 != salones_org[2]:
            salon4=estados[random.randint(0,1)]
            if salon4=="desocupado":
                desocupado_4=desocupado_4+1
            else:
                desocupado_ocupado4=desocupado_ocupado4+1
#__________________________________________________________________________________________________           
            
 
#SALON5________________________________DESOCUPADO___________________________________________      
    if salon5 == "desocupado":
        if salon_5 == salones_org[0]: #Si el salon llega a tener prioridad alta
            if salon1 == "desinfectando" or salon2 == "desinfectando" or salon3 == "desinfectando" or salon4 == "desinfectando":
                bandera_alta5=1;
                salon5="espera"
                desocupado_espera5=desocupado_espera5+1
                if "salon5" in lista: 
                    aaa=1
                else:
                    lista.append("salon5")
            else:
                salon5="desinfectando"
                desocupado_desinfectando5=desocupado_desinfectando5+1
                    
        if salon_5==salones_org[1] or salon_5==salones_org[2]:
            salon5="espera"
            contador_espera5=contador_espera5+1
            desocupado_espera5=desocupado_espera5+1
            if "salon5" in lista: 
                aaa=1
            else:
                lista.append("salon5")
            
        if salon_5 != salones_org[0] and salon_5 != salones_org[1] and salon_5 != salones_org[2]:
            salon5=estados[random.randint(0,1)]
            if salon5=="desocupado":
                desocupado_5=desocupado_5+1
            else:
                desocupado_ocupado5=desocupado_ocupado5+1
#__________________________________________________________________________________________________           

#SALON1_________________--ESPERA--________________
    print(lista)
    if bandera_libre==1:
        prim=lista.pop(0)
        if prim == "salon1":
            salon1="desinfectando"
            espera_desinfectando1=espera_desinfectando1+1
        if prim == "salon2":
            salon2="desinfectando"
            espera_desinfectando2=espera_desinfectando2+1
        if prim == "salon3":
            salon3="desinfectando"
            espera_desinfectando3=espera_desinfectando3+1
        if prim == "salon4":
            salon4="desinfectando"
            espera_desinfectando4=espera_desinfectando4+1
        if prim == "salon5":
            salon5="desinfectando"
            espera_desinfectando5=espera_desinfectando5+1
            
    else:
        if salon1=="espera":
            espera_1=espera_1+1
        if salon2=="espera":
            espera_2=espera_2+1
        if salon3=="espera":
            espera_3=espera_3+1
        if salon4=="espera":
            espera_4=espera_4+1
        if salon5=="espera":
            espera_5=espera_5+1
        
            
#SALON1__________________---DESINFECTANDO---___________________________

    if salon1 == "desinfectando":
        if salon_1 == salones_org[0] or salon_1 == salones_org[1] or salon_1 == salones_org[2]:
            desinfectando_1=desinfectando_1+1
            bandera_libre=0
        else:
            bandera_libre=1
            salon1=estados[random.randint(0,1)]
            if salon1=="desocupado":
                desinfectando_desocupado1=desinfectando_desocupado1+1
            else:
                desinfectando_ocupado1=desinfectando_ocupado1+1
                
                
    if salon2 == "desinfectando":
        if salon_2 == salones_org[0] or salon_2 == salones_org[1] or salon_2 == salones_org[2]:
            desinfectando_2=desinfectando_2+1
            bandera_libre=0
        else:
            bandera_libre=1
            salon2=estados[random.randint(0,1)]
            if salon2=="desocupado":
                desinfectando_desocupado2=desinfectando_desocupado2+1
            else:
                desinfectando_ocupado2=desinfectando_ocupado2+1
                
    if salon3 == "desinfectando":
        if salon_3 == salones_org[0] or salon_3 == salones_org[1] or salon_3 == salones_org[2]:
            desinfectando_3=desinfectando_3+1
            bandera_libre=0
        else:
            bandera_libre=1
            salon3=estados[random.randint(0,1)]
            if salon3=="desocupado":
                desinfectando_desocupado3=desinfectando_desocupado3+1
            else:
                desinfectando_ocupado3=desinfectando_ocupado3+1
                
    if salon4 == "desinfectando":
        if salon_4 == salones_org[0] or salon_4 == salones_org[1] or salon_4 == salones_org[2]:
            desinfectando_4=desinfectando_4+1
            bandera_libre=0
        else:
            bandera_libre=1
            salon4=estados[random.randint(0,1)]
            if salon4=="desocupado":
                desinfectando_desocupado4=desinfectando_desocupado4+1
            else:
                desinfectando_ocupado4=desinfectando_ocupado4+1
                
    if salon5 == "desinfectando":
        if salon_5 == salones_org[0] or salon_5 == salones_org[1] or salon_5 == salones_org[2]:
            desinfectando_5=desinfectando_5+1
            bandera_libre=0
        else:
            bandera_libre=1
            salon5=estados[random.randint(0,1)]
            if salon5=="desocupado":
                desinfectando_desocupado5=desinfectando_desocupado5+1
            else:
                desinfectando_ocupado5=desinfectando_ocupado5+1
                
            
#_______________________________________________________________
#Limpiando Variables
    cont=0
    salones=[]
    salones_org=[]
    
#_________MOSTRANDO RESULTADOS_________________
print("___________________________")
print("salon 1:")
print("Estado ocupado : ",ocupado_1)
print("Estado Desocupado : ",desocupado_1)
print("Estado Espera : ",espera_1)
print("Estado Desinfectando : ",desinfectando_1)


print("Estado Ocupado a Desocupado : ",ocupado_desocupado1)
print("Estado Desocupado a Espera : ",desocupado_espera1)
print("Estado Espera a Desinfectando : ",espera_desinfectando1)
print("Estado Desinfectando a Desocupado : ",desinfectando_desocupado1)
print("Estado Desocupado a Ocupado  : ",desocupado_ocupado1)
print("Estado Desocupado a Desinfectando : ",desocupado_desinfectando1)
print("_________________")

print("___________________________")
print("salon 2:")
print("Estado ocupado : ",ocupado_2)
print("Estado Desocupado : ",desocupado_2)
print("Estado Espera : ",espera_2)
print("Estado Desinfectando : ",desinfectando_2)


print("Estado Ocupado a Desocupado : ",ocupado_desocupado2)
print("Estado Desocupado a Espera : ",desocupado_espera2)
print("Estado Espera a Desinfectando : ",espera_desinfectando2)
print("Estado Desinfectando a Desocupado : ",desinfectando_desocupado2)
print("Estado Desocupado a Ocupado  : ",desocupado_ocupado2)
print("Estado Desocupado a Desinfectando : ",desocupado_desinfectando2)
print("_________________")

print("___________________________")
print("salon 3:")
print("Estado ocupado : ",ocupado_3)
print("Estado Desocupado : ",desocupado_3)
print("Estado Espera : ",espera_3)
print("Estado Desinfectando : ",desinfectando_3)


print("Estado Ocupado a Desocupado : ",ocupado_desocupado3)
print("Estado Desocupado a Espera : ",desocupado_espera3)
print("Estado Espera a Desinfectando : ",espera_desinfectando3)
print("Estado Desinfectando a Desocupado : ",desinfectando_desocupado3)
print("Estado Desocupado a Ocupado  : ",desocupado_ocupado3)
print("Estado Desocupado a Desinfectando : ",desocupado_desinfectando3)
print("_________________")

print("___________________________")
print("salon 4:")
print("Estado ocupado : ",ocupado_4)
print("Estado Desocupado : ",desocupado_4)
print("Estado Espera : ",espera_4)
print("Estado Desinfectando : ",desinfectando_4)


print("Estado Ocupado a Desocupado : ",ocupado_desocupado4)
print("Estado Desocupado a Espera : ",desocupado_espera4)
print("Estado Espera a Desinfectando : ",espera_desinfectando4)
print("Estado Desinfectando a Desocupado : ",desinfectando_desocupado4)
print("Estado Desocupado a Ocupado  : ",desocupado_ocupado4)
print("Estado Desocupado a Desinfectando : ",desocupado_desinfectando4)
print("_________________")

print("___________________________")
print("salon 5:")
print("Estado ocupado : ",ocupado_5)
print("Estado Desocupado : ",desocupado_5)
print("Estado Espera : ",espera_5)
print("Estado Desinfectando : ",desinfectando_5)


print("Estado Ocupado a Desocupado : ",ocupado_desocupado5)
print("Estado Desocupado a Espera : ",desocupado_espera5)
print("Estado Espera a Desinfectando : ",espera_desinfectando5)
print("Estado Desinfectando a Desocupado : ",desinfectando_desocupado5)
print("Estado Desocupado a Ocupado  : ",desocupado_ocupado5)
print("Estado Desocupado a Desinfectando : ",desocupado_desinfectando5)
print("_________________")

#________________________________________________

