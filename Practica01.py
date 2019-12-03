# -*- coding: utf-8 -*-
"""
Primera practica de programacion en Python

Este archivo resume comandos basicos de Python.
"""
#Este tipo de marcado se utiliza para realizar comentarios de una linea

#Uso de los datos primitivos (sin variables)

#Booleanos
# Se pueden probar en la consola de comandos el comportamiento de los datos
# primitivos, es decir aquellos datos que es capaz de manejar el lenguaje

#Declaraciones simples

valor1 = 10
valor2 = 35
valor3 = valor1 + valor2

print ("La suma de ", valor1, " + " , valor2, " = ", valor3)

#Ejemplo empleado funciones

def Sumar(valor1, valor2):
    return valor1+valor2

valor3 = Sumar(valor1, valor2);

print ("La suma de ", valor1, " + " , valor2, " = ", valor3)

valor3 = Sumar(34, 50)

print ("La suma de ", valor1, " + " , valor2, " = ", valor3)

valor1 = 517
valor2 = 1000

valor3 = Sumar(valor1, valor2)

print ("La suma de ", valor1, " + " , valor2, " = ", valor3)

#Que error hay en el codigo anterior?

#Del libro (Bioinformatics Programming)

def Validar_Secuencia_DNA(secuencia):
    secuencia = secuencia.upper()
    return len(secuencia) == (secuencia.count('A') + secuencia.count('C') +
                              secuencia.count('G') + secuencia.count('T'))
    
seq = 'AGCTATCACGGcgtgtacaATCGGGACTTGGGTCAC'

Validez=Validar_Secuencia_DNA(seq)

print ("¿Es una secuencia válida?", Validez)

assert Validez == True, 'No es una secuencia de DNA'   

seq = 'AGCUAUCACGGcgtgtacaAUCGGGACUUGGGUCAC'

Validez=Validar_Secuencia_DNA(seq)

print ("¿Es una secuencia válida?", Validez)   

#Se debe poner atencion en el sangrado (indentation)!!!!

assert Validez == True, 'No es una secuencia de DNA'






