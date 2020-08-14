# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np

## creación de clase 
class Pieza:
    def __init__(self,fila,columna,tipo):       ## atributos de las piezas del juego
        self.fila=fila                          ## fila en la que se encuentra ubicada
        self.columna=columna                    ## columna donde se encuentra ubicada
        self.tipo=tipo                          ## tipo de pieza entre las existentes en el ajedrez
        
    def movimiento(self,fila,columna):         ## función que realiza un cambio de posición en el tablero
        self.fila=fila
        self.columna=columna


## obtener datos

print('El tablero de ajedrez está compuesto por filas y columnas, las filas están enumeradas del 1-8 de manera descendente. Las colunas por otro lado son nombradas con letras de la a-h, a continuación, se muestra un ejemplo: \n')
print(' a  b  c  d  e  f  g  h ')
j=8
for i in range(17):
    
    if (i%2)==0:
        print('-------------------------')
        
    else:
        print('|  |  |  |  |  |  |  |  |',j)
        j=j-1

print('\nEn el ajedrez existen 6 piezas que cuentan con distintas formas de moverse e importancia dentro del juego, a continuación, se enuncian cuales son: ')
print(' 1 rey.\n 2 dama o reina.\n 3 torre.\n 4 alfil.\n 5 caballo.\n 6 peon.\n')

print('Para conocer la posición inicial de la pieza por favor seleccione una columna utilizando la nomenclatura nombrada anteriormente. ')
c=input()
while c!='a' and c!='b' and c!='c' and c!='d' and c!='e' and c!='f' and c!='g' and c!='h':
   print('La opción no es correcta intente nuevamente') 
   c=input()

print('Para conocer la posición inicial de la pieza por favor seleccione una fila utilizando la nomenclatura nombrada anteriormente. ')
f=int(input())
while f!=1 and f!=2 and f!=3 and f!=4 and f!=5 and f!=6 and f!=7 and f!=8:
   print('La opción no es correcta intente nuevamente') 
   f=int(input())
 
print('Seleccione el número del tipo de la pieza de entre las enunciadas anterior mente la cual desea  utilizar:')
t=int(input())
while t!=1 and t!=2 and t!=3 and t!=4 and t!=5 and t!=6:
   print('La opción no es correcta intente nuevamente') 
   t=int(input())



