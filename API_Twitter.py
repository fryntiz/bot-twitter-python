#!/usr/bin/python
# -*- encoding: utf-8 -*-

#######################################
# ###     Raúl Caro Pastorino     ### #
## ##                             ## ##
### # https://github.com/fryntiz/ # ###
## ##                             ## ##
# ###       www.fryntiz.es        ### #
#######################################

##TODO
##Función para dar favorito
##Función para analizar comentarios de un tweet
##Función para retwittear todo lo de un array de personas

#Función para conectar con la API de Twitter
def conectar():
	print('Conectando con la API')
	autenticar = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	autenticar.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(autenticar)

#Función para Publicar en Twitter
def publicar(publicacion):
	print("[+] Twitteando la siguiente entrada...")
	api.update_status(status = line)
	print("[+] Tweet: ", line)
	time.sleep(5)












