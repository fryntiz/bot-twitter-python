#!/usr/bin/python
# -*- encoding: utf-8 -*-

#######################################
# ###     Raúl Caro Pastorino     ### #
## ##                             ## ##
### # https://github.com/fryntiz/ # ###
## ##                             ## ##
# ###       www.fryntiz.es        ### #
#######################################

class Token:
    def __init__(self, ruta):
        archivo_token = ruta + '/token.csv'

        # Leer en "Perfiles/" + perfil + "/token.csv" los valores de API
        tmp_token = open(archivo_token, 'r')
        for line in tmp_token:
            line_clean = line.replace(' ', '').strip().split('=')
            if (line_clean[0].upper() == 'ACCESS_KEY'):
                print('ACCESS_KEY → ' + line_clean[1])
                self.ACCESS_KEY = line_clean[1]
            elif (line_clean[0].upper() == 'ACCESS_SECRET'):
                print('ACCESS_SECRET → ' + line_clean[1])
                self.ACCESS_SECRET = line_clean[1]
            elif (line_clean[0].upper() == 'CONSUMER_KEY'):
                print('CONSUMER_KEY → ' + line_clean[1])
                self.CONSUMER_KEY = line_clean[1]
            elif (line_clean[0].upper() == 'CONSUMER_SECRET'):
                print('CONSUMER_SECRET → ' + line_clean[1])
                self.CONSUMER_SECRET = line_clean[1]