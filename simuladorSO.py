# encoding: utf-8

import json

# Documentación y ambiente

# Estructura del proceso
    # proceso = {
    #     'idproc':0,
    #     'TamanioProceso':0,
    #     'TA':0,
    #     'TI':0
    # }

ltaProcesos = []
# # Estructura de la partición
    # particion ={
    #     'idpart':0,
    #     'tamanioPart':0,
    #     'procesoCargado': proceso,
    #     'fragmentacion':0
    # }

Tcontrol = 0
ltaParticiones = []
maxParticion = 0
controlCarga = 1
colaListos = []
j = 0


#Creamos las particiones que nos pidio la catedra
#Las particiones están en K, no se si escribirlas como 100*1024 o solamente como 100.

#Particion del Sistema Operativo
partAux = {
    'idpart':0,
    'tamanioPart': 100,
    'procesoCargado': 'vacio',
    'fragmentacion': 0
}
ltaParticiones.append(partAux)

#Particion Grande
partAux = {
    'idpart':1,
    'tamanioPart': 250,
    'procesoCargado': 'vacio',
    'fragmentacion': 0
}
ltaParticiones.append(partAux)

#Particion Grande
partAux = {
    'idpart':2,
    'tamanioPart': 120,
    'procesoCargado': 'vacio',
    'fragmentacion': 0
}
ltaParticiones.append(partAux)

#Particion Grande
partAux = {
    'idpart':3,
    'tamanioPart': 60,
    'procesoCargado': 'vacio',
    'fragmentacion': 0
}
ltaParticiones.append(partAux)





"""
------------ Comento esto para ver si lo dejamos o no -------------

# SOLO 3 PARTICIONES
particionesACrear = input('Introduzca el número de particiones a crear: ')
# Creamos las particiones
for part in xrange(1,particionesACrear+1):
    tamanioPart = input('Introduzca tamaño de la partición: ')
    
    # Obtengo mayor particion
    if(maxParticion < tamanioPart):
        maxParticion=tamanioPart

    partAux={
        'idpart':part,
        'tamanioPart':tamanioPart,
        'procesoCargado':'vacio',
        'fragmentacion':0
    }
    ltaParticiones.append(partAux)
"""





print('\n')
print('---------------- Listado de particiones del sistema ----------------\n')    

for elemento in ltaParticiones:
    print('Partición: '+str(elemento['idpart']))
    print('Tamaño de la partición: '+str(elemento['tamanioPart']))
    print('Proceso cargado en partición: '+str(elemento['procesoCargado']))
    print('Fragmentacion interna: '+str(elemento['fragmentacion']))
    print('--------------------------------------------------------------------\n')

#Cargo el SO en la partición 0, como tenemos el SO en la primer parte del arreglo, habría que correr el resto
#de referencias a las particiones en 1
ltaParticiones[0]['procesoCargado']='Sistema Operativo' #Lo agregué como string nomás, tendría que ver esto después

#Como tenemos particiones fijas, defino maxParticion para usarlo después
maxParticion=250

empezando = 1 #Defino una bandera para que muestre un mensaje diferente al inciar

while(controlCarga != 0):
    j=j+1 #Cambie ++j por j=j+1 porque no aumentaba el contador
    if empezando == 1:
        print('A continuacion ingrese la informacion correspondiente al primer proceso')
        empezando = 0
    else:
        controlCarga = input('Escriba 0 para finalizar la carga, cualquier otra cosa para continuar: ')
        if controlCarga == '0': #Puse controlCarga como string porque sino no me lo tomaba y no terminaba nunca el bucle.
            break

    tamanioProctaux = int(input('Introduzca tamaño del proceso: ')) #No tomaba tamanioProctaux porque entraba como string.
    if(maxParticion < tamanioProctaux):
        print('¡¡ERROR!! No hay partición que pueda soportar el proceso actual')
        print('******** RECHAZANDO PROCESO ********\n')
        
        # Ver porque no anda 
        j=j-1
        continue
    #Agrego la conversión a string en TAaux y en TIaux
    TAaux = int(input('Introduzca el tiempo de arribo del proceso: '))
    TIaux = int(input('Introduzca el tiempo de irrupción del proceso: '))

    # Tiempo minimo que se debe ejecutar el sistema 
    Tcontrol = Tcontrol + TIaux
    procesoAux = {
        'idproc':j,
        'TamanioProceso':tamanioProctaux,
        'TA':TAaux,
        'TI':TIaux
    }
    ltaProcesos.append(procesoAux) 

# Ordenar por tiempo de arribo (TA) --> de aca sacar la cola de arribos a memoria
ltaProcesoOrdTA = sorted(ltaProcesos, key = lambda i: (i['TA']))
print(ltaProcesoOrdTA)    
# Ordenar los procesos (sjf): por tiempo de arribo y por TI
subColaListos = sorted(ltaProcesos, key = lambda i: (i['TI'])) #Cola de nuevos procesos
while (Tcontrol != 0 and colaListos ):
    print('¡¡¡¡Empieza simulación!!!!')

# Ir cargando en CPU

# Marcar cuando sale de CPU y que posiocion de memoria se libera

# Indicar cuando no hay mas procesos
