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
        print(nombre, 'Uso el requerimiento de', new_duration, 'de memoria en el tiempo:',env.now)
        tiempoPedir = env.now

         with memoria.request() as turno:
            yield turno
            yield env.timeout(new_duration)
            print(nombre,'Se libero memoria a las',env.now)
            tiempoTotal = env.now - tiempoPedir
            print('%s se tardo %d' % (nombre,tiempoTotal ))
            tiempoMemoria = tiempoMemoria+tiempoTotal

            ready_duration = random.randint(1,10)
        	print(nombre,'va a realizar',ready_duration,'operaciones')

        with operaciones.request() as turno:
            yield turno
            yield env.timeout(ready_duration)
            print (nombre,'termino a las',env.now)
            if ready_duration-3 !=0:
                a = random.randint(1,2)
                if a ==1:
                    Iduration = random.randint(1,3)
                    print(nombre,'realizo', Iduration, 'operaciones adicionales')

                    if a ==2:
                    with operaciones.request() as turno:
                        yield turno
                        yield env.timeout(ready_duration)
                        print (nombre,'termino a las',env.now)
                