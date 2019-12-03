#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 11:23:55 2019

@author: alfonsomt
"""

import os

#Mas sobre funciones, validaciones y valores por defecto

def Validar_Secuencia_AN(secuencia, esRNA=False):
    secuencia = secuencia.upper()
    return len(secuencia) == (secuencia.count('A') + secuencia.count('C') +
                              secuencia.count('G') + 
                              secuencia.count('U' if esRNA else 'T'))

Validez=Validar_Secuencia_AN('ATCGAGCGTA', False)

print (Validez)


Validez=Validar_Secuencia_AN('ATCGAGCGTA', True)

print (Validez)


Validez=Validar_Secuencia_AN('AUCGAGCGUA', True)

print (Validez)

Validez=Validar_Secuencia_AN('AUCGAGCGUA', False)

print (Validez)

#Utilizando modulos disponibles

path=os.getcwd()

print(path)

from os import getcwd as dardirectorio

path2=dardirectorio()

print(path2)
   