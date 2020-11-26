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
colaNuevos = []
j = 0
T = 0
TCpu = 0
cantArribadosenTActual = 0
cpu={
    'libre':True,
    'procesoActual':0,
    'posiocionMemoriaProcesoActual':0,
}
condionEntrada = False
partCandidata = -1
fragmentacionInternaCandidata = 9999
particionesLibres = 0
tiempoEstimadoSimulacion = 0
# variable de control cola de nuevos
x = 0

#Creamos las particiones que nos pidio la catedra
#Las particiones están en K, no se si escribirlas como 100*1024 o solamente como 100.

#Particion del Sistema Operativo
partAux = {
    'idpart':0,
    'tamanioPart': 100,
    'procesoCargado': False,
    'fragmentacion': 0
}
ltaParticiones.append(partAux)

#Particion Grande
partAux = {
    'idpart':1,
    'tamanioPart': 250,
    'particionLibre': True,
    'fragmentacion': 0,
    'idProcesoCargado':0
}
ltaParticiones.append(partAux)

#Particion Grande
partAux = {
    'idpart':2,
    'tamanioPart': 120,
    'particionLibre': True,
    'fragmentacion': 0,
    'idProcesoCargado':0
}
ltaParticiones.append(partAux)

#Particion Grande
partAux = {
    'idpart':3,
    'tamanioPart': 60,
    'particionLibre': True,
    'fragmentacion': 0,
    'idProcesoCargado':0
}
ltaParticiones.append(partAux)
particionesLibres = 3



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
        print('A continuación ingrese la información correspondiente al primer proceso')
        empezando = 0
    else:
        controlCarga = input('Escriba 0 para finalizar la carga, cualquier otra cosa para continuar: ')
        if controlCarga == 0:
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
    tiempoEstimadoSimulacion = tiempoEstimadoSimulacion + TIaux
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

# Obtengo el ultimo proceso que que va a llegar al sistema
ultimoProceso = ltaProcesoOrdTA[-1]
Tcontrol = ultimoProceso['TA'] + ultimoProceso['TI']

print(Tcontrol)    

# Ordenar los procesos (sjf): por tiempo de arribo y por TI
sjf = sorted(ltaProcesos, key = lambda i: (i['TI'])) #Cola de nuevos procesos
print('\n')
print('--------------------------------------------------------------------\n')
print('--------------------------------------------------------------------\n')
print('--------------------------------------------------------------------\n')
print('--------------------------------------------------------------------\n')
print('--------------------------------------------------------------------\n')
print('--------------------------------------------------------------------\n')
print('\n')

print('Procesos que llegaron antes de empezar\n')
print(ltaProcesoOrdTA)
print('\n')
# # Tiempo de simulacion total
# tiempoEstimadoSimulacion = tiempoEstimadoSimulacion + ltaProcesoOrdTA[-1]['TA']

print('--------------------------------------------------------------------\n')
print('- Inico del Simulador\n')
print('- Tiempo Estimado de Simulacion: '+ str(tiempoEstimadoSimulacion))
print('--------------------------------------------------------------------\n')

# while (Tcontrol != T and colaListos): volver a poner este cuando ande los arribos
while True:
    print('\n')
    print('\n')
    print('------------------------- Reloj de Sistema -------------------------')
    print('                               T = '+ str(T))
    print('--------------------------------------------------------------------')
    # Recorro lista de procesos creados y verifico si arriban al Sistema
    for x in xrange(0,len(ltaProcesoOrdTA)):
        if ltaProcesoOrdTA[x]['TA'] == T:
            cantArribadosenTActual = cantArribadosenTActual +1 

    # Verifico Arribos en tiempo actual
    if ltaProcesoOrdTA:
        if ltaProcesoOrdTA[0]['TA'] == T:
            condionEntrada = True
    else:
        condionEntrada = False

    if condionEntrada:
        for y in xrange(0,cantArribadosenTActual):
            # Comprobar todos los arribos en este tiempo T
            if ltaProcesoOrdTA[0]['TA'] <= T:
                print('Agregar a la cola de nuevos --> proceso ID: '+ str(ltaProcesoOrdTA[0]['idproc']) )
                colaNuevos.append(ltaProcesoOrdTA.pop(0))

    # Reinicio cantidad de arribados
    cantArribadosenTActual = 0

    # Mostrar cola de nuevos (darle un formato pretty)
    print('--------------------------------------------------------------------\n')
    print('*************************** Cola Nuevos  ***************************')
    print(colaNuevos)
    print('--------------------------------------------------------------------\n')
    
    

    # Cargar Particiones
    if particionesLibres > 0:
        # Recorro cola de nuevos
        for procesoColaNuevos in xrange(0,len(colaNuevos)):
           
            for z in xrange(1,len(ltaParticiones)):
                if ltaParticiones[z]['particionLibre'] and (ltaParticiones[z]['tamanioPart'] >= colaNuevos[procesoColaNuevos]['TamanioProceso']) and ((ltaParticiones[z]['tamanioPart'] - colaNuevos[procesoColaNuevos]['TamanioProceso']) >=0):
                    # obenter fragmentacion que genera el proceso en esta particion
                    fragmentacionInternaCandidata = ltaParticiones[z]['tamanioPart'] - colaNuevos[procesoColaNuevos]['TamanioProceso']

                    # Obtener ID de la particion candidata
                    partCandidata = ltaParticiones[z]['idpart']

            if partCandidata != -1:
                ltaParticiones[partCandidata]['particionLibre'] = False
                ltaParticiones[partCandidata]['idProcesoCargado'] = colaNuevos[procesoColaNuevos]['idproc']
                ltaParticiones[partCandidata]['fragmentacion'] = fragmentacionInternaCandidata
                colaListos.append(colaNuevos.pop(procesoColaNuevos))
                fragmentacionInternaCandidata = 9999
                partCandidata = -1
                particionesLibres = particionesLibres - 1
            print('Lista de particiones _------------->')
            print(ltaParticiones)
    else:
        print('--------------------------------------------------------------------\n')
        print('********** No hay particiones disponibles en este momento **********')
        print('--------------------------------------------------------------------\n')
        


    # Preguntar si el proceso en ejecución termino
    # if not cpu['libre']:
    #     if  TCpu == 0:
    #         # Mostrar proceso que se va
    #         print('--------------------------------------------------------------------\n')
    #         print('Proceso que sale de CPU al finalizar su ejecución: '+ str(cpu['procesoActual']))
    #         print('--------------------------------------------------------------------\n')
        
    #         # Liberar CPU
    #         cpu['libre'] = True

    #         # Desasignar RAM
    #         for x in xrange(1,len(ltaParticiones)):
    #             if ltaParticiones[x]['idProcesoCargado'] == cpu['procesoActual']:
    #                 print('--------------------------------------------------------------------\n')
    #                 print('----------------Se desaloja de la partición:' + str(ltaParticiones[x]['idpart']) + '----------------')
    #                 print('--------------------------------------------------------------------\n')
    #                 ltaParticiones[x]['particionLibre'] = True
    #                 ltaParticiones[x]['idProcesoCargado'] = 0
    #                 ltaParticiones[x]['fragmentacion'] = 0
    #                 particionesLibres = particionesLibres + 1
    #                 print('--------------------------------------------------------------------\n')
    #     else: 
    #         TCpu = TCpu -1
    #         tiempoEstimadoSimulacion = tiempoEstimadoSimulacion -1
    #         print('--------------------------------------------------------------------\n')
    #         print('********** Proceso ejecutandose en CPU **********')
    #         print('- ID Proceso en CPU: ' + str(cpu['procesoActual']))
    #         print('- Tiempo restante en CPU: ' + str(TCpu))
    #         print('--------------------------------------------------------------------\n')


###########################################################################################################################

    if not cpu['libre']:
        TCpu = TCpu -1
        tiempoEstimadoSimulacion = tiempoEstimadoSimulacion -1
        print('--------------------------------------------------------------------\n')
        print('******************* Proceso ejecutandose en CPU *******************')
        print('- ID Proceso en CPU: ' + str(cpu['procesoActual']))
        print('- Tiempo restante en CPU: ' + str(TCpu))
        print('\n')
        print('--------------------------------------------------------------------\n')
        
        if  TCpu == 0:
            # Mostrar proceso que se va
            print('--------------------------------------------------------------------\n')
            print('Proceso que sale de CPU al finalizar su ejecución: '+ str(cpu['procesoActual']))
            print('--------------------------------------------------------------------\n')
            # Liberar CPU
            cpu['libre'] = True
            # Desasignar RAM
            for x in xrange(1,len(ltaParticiones)):
                if ltaParticiones[x]['idProcesoCargado'] == cpu['procesoActual']:
                    print('\n')
                    print('----------------- Se desaloja de la partición:' + str(ltaParticiones[x]['idpart']) + ' --------------------')
                    print('--------------------------------------------------------------------\n')
                    ltaParticiones[x]['particionLibre'] = True
                    ltaParticiones[x]['idProcesoCargado'] = 0
                    ltaParticiones[x]['fragmentacion'] = 0
                    particionesLibres = particionesLibres + 1
                    print('--------------------------------------------------------------------\n')



    # Preguntar si el CPU esta libre y asignar proceso de ser asi
    print('--------------------------- COLA LISTOS ----------------------------')

    print(colaListos)
    colaListos = sorted(colaListos, key = lambda i: (i['TI']))

    if cpu['libre'] and colaListos:
        print('--------------------------------------------------------------------\n')
        print('------------- CPU LIBRE, se asigna el proceso ID: ' + str(colaListos[0]['idproc']) + ' ----------------')
        print('--------------------------------------------------------------------\n')
        
        TCpu = colaListos[0]['TI']
        cpu['procesoActual'] = colaListos[0]['idproc']
        cpu['libre'] = False
        colaListos.pop(0)


    # Sumar 1 al reloj del sistema
    T=T+1
    if tiempoEstimadoSimulacion == 0:
        break

print('\n')
print('¡¡¡Simulación Terminada!!!\n')
print('Gracias por usar el simulador planificación de procesos y gestión de colas\n')
print('Grupo 3, Sistemas Operativos\n')
print('UTN - FRRe - 2020\n')