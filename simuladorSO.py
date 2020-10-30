# encoding: utf-8

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
print('\n')
print('---------------- Listado de particiones del sistema ----------------\n')    
  
for elemento in ltaParticiones:
    print('Partición: '+str(elemento['idpart']))
    print('Tamaño de la partición: '+str(elemento['tamanioPart']))
    print('Proceso cargado en partición: '+str(elemento['procesoCargado']))
    print('Fragmentacion interna: '+str(elemento['fragmentacion']))
    print('--------------------------------------------------------------------\n')

# A priori, por simplicidad se restringe la carga como tope a tantos procesos como particiones haya en el sistema. 
print('NOTA: Al momento solo se pueden cargar como tope, tantos procesos como particiones haya\n')
while(controlCarga != 0):
    ++j
    controlCarga = input('Si desea cargar un proceso presione 1 en caso contrario presione 0 para terminar la carga: ')
    if controlCarga == 0:
        break

    tamanioProctaux = input('Introduzca tamaño del proceso: ')
    if(maxParticion < tamanioProctaux):
        print('¡¡ERROR!! No hay partición que pueda soportar el proceso actual')
        print('******** RECHAZANDO PROCESO ********\n')
        
        # Ver porque no anda esta mierda 
        j=j-1
        continue

    TAaux = input('Introduzca el tiempo de arribo del proceso: ')
    TIaux = input('Introduzca el tiempo de irrupción del proceso: ')

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
subColaListos = 
while (Tcontrol != 0 and colaListos ):
    print('¡¡¡¡Empieza simulación!!!!')

# Ir cargando en CPU

# Marcar cuando sale de CPU y que posiocion de memoria se libera

# Indicar cuando no hay mas procesos


