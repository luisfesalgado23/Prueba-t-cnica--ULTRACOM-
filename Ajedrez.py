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
        self.tablero=np.zeros((8,8))            ## creación del tablero
        
    def movimiento(self,fila,columna):          ## función que realiza un cambio de posición en el tablero
        if self.tablero[fila][columna]==0:
            print('El movimiento no es valido')
            
        else:
            self.fila=fila
            self.columna=columna
            for i in range(8):                      ## restaurar los valores del tablero
                for j in range(8):
                    self.tablero[i][j]=0
    
    def diagonal(self):                                 ## funcion que llena los movimientos en diagnal

        i=8-self.fila
        j=self.columna-1


        self.tablero[i][j]=8
    
        while j<7 and i>0:             ## llenando diagonal superior derecha
            self.tablero[i-1][j+1]=1
            i=i-1
            j=j+1
        
        i=8-self.fila
        j=self.columna-1
    
        while j>0 and i>0:             ## llenando diagonal superior izquierda
            self.tablero[i-1][j-1]=1
            i=i-1
            j=j-1
        
        i=8-self.fila
        j=self.columna-1
    
        while j>0 and i<7:             ## llenando diagonal inferior izquierda
            self.tablero[i+1][j-1]=1
            i=i+1
            j=j-1
        
        i=8-self.fila
        j=self.columna-1
    
        while j<7 and i<7:             ## llenando diagonal inferior derecha
            self.tablero[i+1][j+1]=1
            i=i+1
            j=j+1

    def ver_hor(self):
        i=8-self.fila
        j=self.columna-1
    
        for k in range(8):             ## llenando columna
            self.tablero[i][k]=1
      
        for k in range(8):             ## llenando fila
            self.tablero[k][j]=1
           
        self.tablero[i][j]=8        
        
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

#%%

pieza = Pieza(f, ord(c)-96, t)

if pieza.tipo==4:
    pieza.diagonal()
    
if pieza.tipo==3:
    pieza.ver_hor()

if pieza.tipo==2:
    pieza.diagonal()
    pieza.ver_hor()
    
print (pieza.tablero)