#!/usr/bin/python
# -*- encoding: utf-8 -*-

#######################################
# ###     Raúl Caro Pastorino     ### #
## ##                             ## ##
### # https://github.com/fryntiz/ # ###
## ##                             ## ##
# ###       www.fryntiz.es        ### #
#######################################

# Este script se está planteando para muchos perfiles pero se bloqueará
# hasta llegar a un punto más avanzado a solo 1 perfil (posición 0 en array's)'

##############################
##    Importar Librerías    ##
##############################
import time  # Importamos la libreria time --> time.sleep
#import sys  # Importar comandos del sistema, por ejemplo exit
import os  # Importar lib para interactuar con el sistema
#import random  # Genera números aleatorios --> random.randrange(1,100)
import convert_ODS  # Importa de este directorio el script para convertir a CSV
from API_TWITTER import API_TWITTER
from publicacion import publicacion
#from VAR import *  # importar todas las variables

##############################
##         Variables        ##
##############################
sleep = time.sleep  # variable para usar con más comodidad el control de tiempo
PERFILES = ''
ENTRADAS = ''


# Array con cada objeto perfil (clase API_TWITTER)
def crear_perfiles():
    global PERFILES
    PERFILES = [API_TWITTER(0, "perfil1", "asd", "asd", "asd", "asd")]
crear_perfiles()


#Función a la que se pasa un nombre o ruta hacia archivo y devuelve booleano
def existe_archivo(ruta_archivo):
    return os.path.isfile(ruta_archivo)  # Comprobar que existe


#Convertir a CSV el archivo ODS. Por defecto busca "Publicar.ods"
def inicializar():
    #Llamar desde aquí a crear_perfiles()
    global ENTRADAS
    print('\n[+]Buscando archivo → Publicar.ods')
    if existe_archivo('Publicar.ods'):
        print('[+]Utilizando el Archivo Publicar.ods')
        # Convertir ODS en CSV
        convert_ODS.toCSV("Publicar.ods")
    # TOFIX → Si no existe Publicar.ods se almacena en "ARCHIVO_ENTRADA"
    # pero no es del todo claro. Plantear dar aviso e ignorar perfil y publicns
    #else:
    #    print('[~]Archivo Publicar.ods no encontrado')
    #    ARCHIVO_ENTRADA = raw_input('Ruta completa hasta el archivo: ')

    #Se comprueba que el CSV se ha creado antes de intentar crear objetos
    if existe_archivo('Publicar.csv'):
        # Array con cada entrada. La posición coincide con posición en PERFILES
        ENTRADAS = [publicacion("Publicar.csv")]
inicializar()


# Publicar
def publicar():
    print('[+] Preparando para publicar')


# Retwittear
def retwittear():
    print('[+] Preparando para retwittear')


# Seguir
def seguir():
    print('[+] Preparando para seguir')


# Programa principal para interactuar con el bot
def panel_control():
    print('Elige una opción de las siguientes (No Implementado')
#panel_control()


# Depuración del programa
def depurador():
    print('Se ha ejecutado el modo depurador (No Implementado)')


#Función de pruebas 1 → Muestra cada publicación sin publicarla
def test0():
    #Bucle temporal para crear la cadena a publicar a partir de la línea
    while True:
        print('\n[+] Entrada Publicada:\n' + ENTRADAS[0].publicacion_actual())
        ENTRADAS[0].siguiente_linea()
        sleep(5)
test0()


#Función para solo publicar cada 1h mientras se prueba funcionamiento
def test1():
    while True:
        print('\n[+] Entrada Publicada:\n' + ENTRADAS[0].publicacion_actual())
        ENTRADAS[0].siguiente_linea()
        sleep(7200)  # 2 Horas entre publicaciones
#test1


#Función para publicar cada 6 horas
def test2():
    while True:
        print('\n[+] Entrada Publicada:\n' + ENTRADAS[0].publicacion_actual())
        ENTRADAS[0].siguiente_linea()
        sleep(21600)  # 6 Horas entre publicaciones
#test2


#Obtiene el timeline agregándolo a un archivo
def test3():
    print('Conectando API')
    print('Obteniendo timeline')
    print('Pasándolo al archivo XXXX')
#test3

#Preparando para cerrar script → print('\n[+]Cerrando Script')