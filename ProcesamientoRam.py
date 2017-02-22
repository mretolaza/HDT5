#ProcesamientoRam.py
#Maria Mercedes Retolaza Reyna 
#Carne 16339, Seccion 20 
#Algortimos y Estructura de Datos 
#El programa se encarga de simular como funciona una memoria RAM a un entorno, se crean diferentes procesos 
#En un espacio de memoria dado, el objetivo es ver cuanto a almacenado a la cola y asi identificar que tipo es 
# mas rapido 


#Se importan las librerias random y simpy para realizar el simualdor 
import simpy  
import random

def operacion(nombre,env,memoria):
    global tiempoMemoria
    while True:
        new_duration = random.randint(1,10)
        print(nombre, 'pidio', new_duration, 'de memoria en el tiempo:',env.now)
        tiempoPedir = env.now

         with memoria.request() as turno:
            yield turno
            yield env.timeout(new_duration)
            print(nombre,'libero memoria a las',env.now)
            tiempoTotal = env.now - tiempoPedir
            print('%s se tardo %d' % (nombre,tiempoTotal ))
            tiempoMemoria = tiempoMemoria+tiempoTotal