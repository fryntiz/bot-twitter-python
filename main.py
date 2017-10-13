#!/usr/bin/python
# -*- encoding: utf-8 -*-

#################################################
# ###                                     Raúl Caro Pastorino                                     ### #
## ##                                                                                                         ## ##
### #                                 https://github.com/fryntiz/                                # ###
## ##                                                                                                         ## ##
# ###                                         www.fryntiz.es                                         ### #
#################################################

# Este script se está planteando para muchos perfiles distintos pero se bloqueará
# hasta llegar a un punto más avanzado a solo 1 perfil (posición 0 en array's)'

##############################
##                    Importar Librerías                    ##
##############################
import time  # Importamos la libreria time --> time.sleep
import sys  # Importar comandos del sistema, por ejemplo exit
import os  # Importar lib para interactuar con el sistema
import random  # Genera números aleatorios --> random.randrange(1,100)
import convert_ODS  # Importa de este directorio el script para convertir a CSV
from VAR import *  # importar todas las variables

##############################
##         Variables        ##
##############################
sleep = time.sleep  # variable para usar con más comodidad el control de tiempo


# Array con cada objeto perfil
PERFILES[0] = API_TWITTER(0, "perfil1", "asd", "asd", "asd", "asd")

#Convertir a CSV el archivo ODS. Por defecto busca "Publicar.ods"
def inicializar():
    print('\n[+]Buscando archivo → Publicar.ods')
    if existe_archivo(Publicar.ods):
        print('[+]Utilizando el Archivo Publicar.ods')
        # Convertir ODS en CSV
        convert_ODS.toCSV("Publicar.ods")
    else:
        print('[~]Archivo Publicar.ods no encontrado')
        ARCHIVO_ENTRADA = raw_input('Ruta completa hasta el archivo: ')

    # Array con cada entradas. La posición coincide con posición en PERFILES
    ENTRADAS[0] = publicacion("Publicar.csv")
inicializar()


#Conectar a la API de Twitter
#Probablemente sobre esta función
def conectar_Twitter():
    print('\n[+]Conectando con la API de Twitter')
    print('[+]Espera un momento mientras se establece la conexión')

    tmp = 0
    while tmp <= 10:
        try:
            print('[+]Llamar a la función para conectar')
            API_Twitter.conectar()
        except:
            tmp = tmp + 1
            print('[-]No se ha conectado a la API de Twitter, reintento ', tmp)
            if tmp < 10:
                print('[~]Se reintentará en 3 segundos')
                sleep(3)
            elif tmp == 10:
                print('[-]Se han realizado 10 intentos de conexión sin éxito')
    print('[Se reintentará más tarde')
#conectar_Twitter() #DESCOMENTAR PARA EJECUTAR


# Publicar
def publicar():
    print('[+] Preparando para publicar')

# Retwittear
def retwittear():
    print('[+] Preparando para retwittear')

# Seguir
def seguir():
    print('[+] Preparando para seguir')





#Función de pruebas 1 → Muestra cada publicación sin publicarla
def test0():
    #Bucle temporal para crear la cadena a publicar a partir de la línea
    while True:
        print ("[+] Entrada " + str(LINEA_ACTUAL) + " → " + ARRAY_ENTRADAS[LINEA_ACTUAL])
        siguiente_linea()
        sleep(5)
test0()


#Función para solo publicar cada 1h mientras se prueba funcionamiento
def test1():
    while True:
        conectar_Twitter()
        API_Twitter.publicar(ARRAY_ENTRADAS[LINEA_ACTUAL])
        siguiente_linea()
        sleep(7200)  # 2 Horas entre publicaciones
#test1


#Función para publicar cada 6 horas
def test2():
    while True:
        conectar_Twitter()
        API_Twitter.publicar(ARRAY_ENTRADAS[LINEA_ACTUAL])
        siguiente_linea()
        sleep(21600)  # 6 Horas entre publicaciones
#test2



#Twittear 1 entrada cada X minutos (2 en total)

#Agregar 1 favorito cada X minutos (3 en total)

#Retwittear 1 twitt cada X minutos (5 en total)

#Estructura para controlar el tiempo total que trabajará el bot (o hasta infinito)

#Preparando para cerrar
#print('\n[+]Cerrando Script')
#ARCHIVO_CSV.close()
