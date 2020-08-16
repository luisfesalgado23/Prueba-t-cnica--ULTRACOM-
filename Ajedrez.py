# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

## creación de clase 
class Pieza:
    def __init__(self,fila,columna,tipo):          ## atributos de las piezas del juego
        self.fila=fila                                  ## fila en la que se encuentra ubicada
        self.columna=columna                            ## columna donde se encuentra ubicada
        self.tipo=tipo                                  ## tipo de pieza entre las existentes en el ajedrez
        self.tablero=np.zeros((8,8))                    ## creación del tablero
        
    def movimiento(self,fil,colum):                  ## función que realiza un cambio de posición en el tablero
        i=8-fil                                         ## fila en la matriz
        j=colum-1                                       ## columna en la matriz
        if self.tablero[i][j]==0:      
            print('El movimiento no es valido \n')
            
        else:
            self.fila=fil
            self.columna=colum
            for i in range(8):                          ## restaurar los valores del tablero
                for j in range(8):
                    self.tablero[i][j]=0
    
    def diagonal(self):                                 ## funcion que llena los movimientos en diagnal

        i=8-self.fila
        j=self.columna-1


        self.tablero[i][j]=8
    
        while j<7 and i>0:                              ## llenando diagonal superior derecha
            self.tablero[i-1][j+1]=1
            i=i-1
            j=j+1
        
        i=8-self.fila
        j=self.columna-1
    
        while j>0 and i>0:                             ## llenando diagonal superior izquierda
            self.tablero[i-1][j-1]=1
            i=i-1
            j=j-1
        
        i=8-self.fila
        j=self.columna-1
    
        while j>0 and i<7:                             ## llenando diagonal inferior izquierda
            self.tablero[i+1][j-1]=1
            i=i+1
            j=j-1
        
        i=8-self.fila
        j=self.columna-1
    
        while j<7 and i<7:                             ## llenando diagonal inferior derecha
            self.tablero[i+1][j+1]=1
            i=i+1
            j=j+1

    def ver_hor(self):                              ## funcion para movimientos verticales y horizontales
        i=8-self.fila
        j=self.columna-1
    
        for k in range(8):                            ## llenando columna
            self.tablero[i][k]=1
      
        for k in range(8):                            ## llenando fila
            self.tablero[k][j]=1
           
        self.tablero[i][j]=8        

    def rey(self):                                  ## funcion que llena los movimientos para el rey
        i=8-self.fila
        j=self.columna-1
    
        if i!=0 and i!=7 and j!=0 and j!=7:         ##cualquier posicion fuera de los extremos
            for k in range(3):
                for n in range(3):
                    self.tablero[i+k-1][j+n-1]=1
            self.tablero[i][j]=8
        
        if i==0 and j==0:                           ## esquina inferior izquierda
            for k in range(2):
                for n in range(2):
                    self.tablero[i+k][j+n]=1
            self.tablero[i][j]=8
        
        if i==7 and j==0:                           ## esquina superior izquierda
            for k in range(2):
                for n in range(2):
                    self.tablero[i+k-1][j+n]=1
            self.tablero[i][j]=8
        
        if i==0 and j==7:                           ## esquina inferior derecha del tablero
            for k in range(2):
                for n in range(2):
                    self.tablero[i+k][j+n-1]=1
            self.tablero[i][j]=8
        
        if i==7 and j==7:                           ## esquina superior derecha del tablero
            for k in range(2):
                for n in range(2):
                    self.tablero[i+k-1][j+n-1]=1
            self.tablero[i][j]=8
        
        if i==0 and j!=0 and j!=7:                  ## extremo inferior del tablero             
            for k in range(2):
                for n in range(3):
                    self.tablero[i+k][j+n-1]=1
            self.tablero[i][j]=8
        
        if i==7 and j!=0 and j!=7:                  ## extremo superior del tablero
            for k in range(2):
                for n in range(3):
                    self.tablero[i+k-1][j+n-1]=1
            self.tablero[i][j]=8
        
        if j==0 and i!=0 and i!=7:                  ## extremo izquierdo del tablero
            for k in range(3):
                for n in range(2):
                    self.tablero[i+k-1][j+n]=1
            self.tablero[i][j]=8
        
        if j==7 and i!=0 and i!=7:                  ## extremo derecho del tablero
            for k in range(3):
                for n in range(2):
                    self.tablero[i+k-1][j+n-1]=1
            self.tablero[i][j]=8
    
    def caballo(self):                              ## funcion para los movimientos del caballo
        i=8-self.fila
        j=self.columna-1
        bandera =0
    
    ## region 1 para movimientos del caballo
    
        if j>1 and j<6 and i>1 and i<6:
            for k in range(0,5,4):
                for n in range(0,3,2):
                    self.tablero[i+k-2][j+n-1]=1
            for k in range(0,3,2):
                for n in range(0,5,4):
                    self.tablero[i+k-1][j+n-2]=1
            self.tablero[i][j]=8

    ## region 2 para movimientos del caballo

        if i>1 and i<6:
        
            if j==1:
                m=2
                bandera=1
            if j==6:
                m=-2
                bandera=2
            if bandera==1:
                for k in range(0,5,4):
                    for n in range(0,3,2):
                        self.tablero[i+k-2][j+n-1]=1
                for n in range(0,3,2):
                    self.tablero[i+n-1][j+m]=1
                self.tablero[i][j]=8
                bandera=0
            
            if j>1 and j<6:
        
                if i==1:
                    m=2
                    bandera=1
                if i==6:
                    m=-2
                    bandera=1
                if bandera==1:
                    for n in range(0,3,2):
                        self.tablero[i+m][j+n-1]=1
                    for k in range(0,3,2):
                        for n in range(0,5,4):
                            self.tablero[i+k-1][j+n-2]=1
                    self.tablero[i][j]=8
                    bandera=0
     
            
         ## region 4 para movimientos del caballo
        if i>1 and i<6:
        
             if j==0:
                 m=2
                 o=1
                 bandera=1
             if j==7:
                m=-2
                o=-1
                bandera=1
             if bandera==1:
                 for k in range(0,5,4):
                     self.tablero[i+k-2][j+o]=1
                 for n in range(0,3,2):
                     self.tablero[i+n-1][j+m]=1
                 self.tablero[i][j]=8
                 bandera=0

        if j>1 and j<6:
        
             if i==0:
                 m=2
                 o=1
                 bandera=1
             if i==7:
                 m=-2
                 o=-1
                 bandera=1
             if bandera==1:
                for n in range(0,5,4):
                    self.tablero[i+o][j+n-2]=1
                for n in range(0,3,2):
                    pieza.tablero[i+m][j+n-1]=1
                self.tablero[i][j]=8
                bandera=0
    
    ## region 3 para movimientos del caballo
    
        if i==j:
            if j==1:
               o=2
               bandera=1
            if j==6:
                o=-2
                bandera=1
            
            if bandera==1:
                for n in range(0,3,2):
                    self.tablero[i+o][j+n-1]=1
                for n in range(0,3,2):
                    self.tablero[i+n-1][j+o]=1    
                self.tablero[i][j]=8  
                bandera=0
        
            
        if i==1 and  j==6:
            for n in range(0,3,2):
                self.tablero[i+2][j+n-1]=1
            for n in range(0,3,2):
                self.tablero[i+n-1][j-2]=1    
            self.tablero[i][j]=8  
            
        if i==6 and  j==1:
            for n in range(0,3,2):
                self.tablero[i-2][j+n-1]=1
            for n in range(0,3,2):
                self.tablero[i+n-1][j+2]=1    
            self.tablero[i][j]=8      
     
   ### region 5 para movimientos del caballo
   
        if j==0 or j==7:
            if j==0:
                u=1
            if j==7:
                u=-1
            if i==1:
                o=2
                bandera=1
            if i==6:
                o=-2
                bandera=1
            if bandera==1:
                for n in range(0,3,2):
                    self.tablero[i+n-1][j+(2*u)]=1
                self.tablero[i+o][j+(1*u)]=1
                self.tablero[i][j]=8
    
        if i==0 or i==7:
            if i==0:
                u=1
            if i==7:
                u=-1
            if j==1:
                o=2
                bandera=1
            if j==6:
                o=-2
                bandera=1
            if bandera==1:
                for n in range(0,3,2):
                    self.tablero[i+(2*u)][j+n-1]=1
                self.tablero[i+(1*u)][j+o]=1
                self.tablero[i][j]=8
    
    
   ### region 6 para movimientos del caballo 
    
        if i==j:
            if j==0:
                o=1
                bandera=1
            if j==7:
                o=-1
                bandera=1
            if bandera==1:
                self.tablero[i+(2*o)][j+(1*o)]=1
                self.tablero[i+(1*o)][j+(2*o)]=1    
                self.tablero[i][j]=8
                bandera=0
    
        if i==0 and  j==7:
            self.tablero[i+(2)][j-(1)]=1
            self.tablero[i+(1)][j-(2)]=1    
            self.tablero[i][j]=8  
            
        if i==7 and  j==0:
            self.tablero[i-(2)][j+(1)]=1
            self.tablero[i-(1)][j+(2)]=1    
            self.tablero[i][j]=8
        
    def peon(self):
        i=8-self.fila
        j=self.columna-1
        
        if i==7 or i>0 and i<6:
            self.tablero[i-1][j]=1
            self.tablero[i][j]=8
        
        if i==6:
            for n in range(2):
                self.tablero[i-n-1][j]=1
            self.tablero[i][j]=8
        
        if i==0:
            print('Su peón tiene la oportunidad de coronarse. Cual de las siguientes pieza elige:\n2 dama o reina.\n 3 torre.\n 4 alfil.\n 5 caballo.\n ')
            t=input()
            while  t!='2' and t!='3' and t!='4' and t!='5':
                print('La opción no es correcta intente nuevamente') 
                t=input()
            self.tipo=int(t)

## funciones

def imp_datos(mat):                                 ## funcion para mostrar en pantalla los datos de manera ordenada
    print('  a   b   c   d   e   f   g   h ')
    j=8
    for i in range(17):
        if (i%2)==0:
            print('---------------------------------')
        else:
            print('| {} | {} | {} | {} | {} | {} | {} | {} | {}'.format(int(mat[8-j][0]),int(mat[8-j][1]),int(mat[8-j][2]),int(mat[8-j][3]),int(mat[8-j][4]),int(mat[8-j][5]),int(mat[8-j][6]),int(mat[8-j][7]), j))
            j=j-1

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
f=input()
while f!='1' and f!='2' and f!='3' and f!='4' and f!='5' and f!='6' and f!='7' and f!='8':
   print('La opción no es correcta intente nuevamente') 
   f=input()
 
print('Seleccione el número del tipo de la pieza de entre las enunciadas anterior mente la cual desea  utilizar:')
t=input()
while t!='1' and t!='2' and t!='3' and t!='4' and t!='5' and t!='6':
   print('La opción no es correcta intente nuevamente') 
   t=input()

## cuerpo

pieza = Pieza(int(f), ord(c)-96, int(t))
bandera=1
ejecutar='0'
while ejecutar!='1':
    
    if bandera == 1:
        print('¿que desea hacer? \n 1= Salir. \n 2= Ver movimientos. \n')
        ejecutar=input()
        while ejecutar!='1' and ejecutar!='2':
            print('La opción no es correcta intente nuevamente') 
            ejecutar=input()
        bandera=0
        
        if ejecutar=='2':    ## Mostrar movimientos para las piezas   
            if pieza.tipo==1:
                pieza.rey()
                imp_datos(pieza.tablero)
            if pieza.tipo==2:
                pieza.diagonal()
                pieza.ver_hor()
                imp_datos(pieza.tablero)
            if pieza.tipo==3:
                pieza.ver_hor()
                imp_datos(pieza.tablero)
            if pieza.tipo==4:
                pieza.diagonal()
                imp_datos(pieza.tablero)
            if pieza.tipo==5:
                pieza.caballo() 
                imp_datos(pieza.tablero)
            if pieza.tipo==6:
                pieza.peon()
                if pieza.fila!=8:
                    imp_datos(pieza.tablero)
                else:
                    bandera=1
        if ejecutar=='3':                         ## realizar movimiento con una pieza
            print('Para conocer la posición de la pieza por favor seleccione una columna utilizando la nomenclatura. ')
            c=input()
            while c!='a' and c!='b' and c!='c' and c!='d' and c!='e' and c!='f' and c!='g' and c!='h':
                print('La opción no es correcta intente nuevamente') 
                c=input()

            print('Para conocer la posición de la pieza por favor seleccione una fila utilizando la nomenclatura. ')
            f=input()
            while f!='1' and f!='2' and f!='3' and f!='4' and f!='5' and f!='6' and f!='7' and f!='8':
                print('La opción no es correcta intente nuevamente') 
                f=input()
            pieza.movimiento(int(f), ord(c)-96)
            bandera=1
    
    if bandera == 0:
        ejecutar=input('¿Que desea hacer? \n 1= Salir. \n 2= Ver movimientos \n 3= Realizar un movimiento')
        while ejecutar!='1' and ejecutar!='2' and ejecutar!='3':
            print('La opción no es correcta intente nuevamente') 
            ejecutar=input()
        
        if ejecutar=='2':                     ##mostrar movimiento con una pieza     
            if pieza.tipo==1:
                pieza.rey()
                imp_datos(pieza.tablero)                       
            if pieza.tipo==2:
                pieza.diagonal()
                pieza.ver_hor()
                imp_datos(pieza.tablero)
            if pieza.tipo==3:
                pieza.ver_hor()
                imp_datos(pieza.tablero)
            if pieza.tipo==4:
                pieza.diagonal()
                imp_datos(pieza.tablero)
            if pieza.tipo==5:
                pieza.caballo() 
                imp_datos(pieza.tablero)
            if pieza.tipo==6:
                pieza.peon()
                if pieza.fila!=8:
                    imp_datos(pieza.tablero)
                else:
                    bandera=1
        if ejecutar=='3':                     ## realizar movimiento con una pieza
            print('Para conocer la posición de la pieza por favor seleccione una columna utilizando la nomenclatura. ')
            c=input()
            while c!='a' and c!='b' and c!='c' and c!='d' and c!='e' and c!='f' and c!='g' and c!='h':
                print('La opción no es correcta intente nuevamente') 
                c=input()

            print('Para conocer la posición de la pieza por favor seleccione una fila utilizando la nomenclatura. ')
            f=input()
            while f!='1' and f!='2' and f!='3' and f!='4' and f!='5' and f!='6' and f!='7' and f!='8':
                print('La opción no es correcta intente nuevamente') 
                f=input()
            pieza.movimiento(int(f), ord(c)-96)
            bandera=1