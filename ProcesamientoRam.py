#ProcesamientoRam.py
#Maria Mercedes Retolaza Reyna 
#Carne 16339, Seccion 20 
#Algortimos y Estructura de Datos 


#Se importan las librerias random y simpy para realizar el simualdor 
import simpy  
import random

def operacion(nombre,env,memoria):
    global tiempoMemoria
    while True:
        new_duration = random.randint(1,10)
        print(nombre, 'pidio', new_duration, 'de memoria en el tiempo:',env.now)
        tiempoPedir = env.now