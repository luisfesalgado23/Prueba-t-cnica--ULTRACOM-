# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 09:55:54 2020

@author: Usuario
"""

import numpy as np
    
class Polinomio:
    def __init__(self,grado,coef):
        self.grado=grado                ## grado del polinomio, sera el valor del mayor exponente
        self.coef=coef                  ## coeficientes del polinomio
        
    def suma_resta(self,pol2,op):
        ## la resta se hace recibiendo un objeto de tipo polinomio el cual sera el portador del signo negativo en la operacion
        ## op sera la opcion de ser una suma si vale 1, una resta en cualquier otro caso
        
        if pol2.grado>self.grado:  ## encontrando el polinomio con el mayor grado
           may=len(pol2.coef)
           men=len(self.coef)
           coef_may=pol2.coef
           coef_men=self.coef
           if op==1:
               smay=1                       ## signo que tiene el polinomio mayor
               smen=1                      ## signo que tiene el polinomio menor
           else:
               smay=-1                       ## signo que tiene el polinomio mayor
               smen=1                      ## signo que tiene el polinomio menor
        
        else :#: ## encontrando el polinomio con el mayor grado
           men=len(pol2.coef)
           may=len(self.coef)
           coef_men=pol2.coef
           coef_may=self.coef
           if op==1:
               smay=1                       ## signo que tiene el polinomio mayor
               smen=1                      ## signo que tiene el polinomio menor
           else:
               smay=1                       ## signo que tiene el polinomio mayor
               smen=-1                      ## signo que tiene el polinomio menor
                   
        new_coef=np.zeros(may)              ## variabe para guardar los resultados de la operacion.
        for i in range(may):
            if i>=men:
               new_coef[may-i-1]=coef_may[may-i-1]*smay   ##rellenar los coeficientes que no tienen con quien restarse por tener un grado mayor al de otro polinomio
            else:
               new_coef[may-i-1]=coef_may[may-i-1]*smay+coef_men[men-i-1]*smen  ##resta de los coeficientes del mismo grado
        return Polinomio(may, new_coef)     ## se devuelve un polimo que es el resultado de la operacion seleccionada
 
    
    def mult_poli(self,pol2):                           ## multiplicacion de polinomios
        new_coef=np.zeros((self.grado+pol2.grado)+1)   ## arreglo para guardar los nuevos coeficientes
        y=0
        for i in range(len(self.coef)):                 ## se replica la ley distributiva
            for j in range(len(pol2.coef)):
                y=self.coef[i]*pol2.coef[j]             ## se deja quieto un valor del polinomio uno y se cambian los del 2 
                new_coef[i+j]=new_coef[i+j]+y          ## se van guardndo los valores la posicion que corresponde a su exponente, se suman todos los resultados de un mismo exponente
        
        return Polinomio(self.grado+pol2.grado, new_coef)
    
    def mult_esca(self,esc):
        new_coef=np.zeros(len(self.coef))   ## arreglo para guardar los nuevos coeficientes
        
        for i in range(len(self.coef)):
            new_coef[i]=self.coef[i]*esc                ##multiplacando el escalar por el coeficiente n-i
            
        return Polinomio(self.grado,new_coef)           ## se decuelve un polinomio con los nuevos coeficientes y el miso grado
            
    def evaluar(self,x):
        ## x es el valor que se le dio a la variable del polinomio para ser evaluado
        y=0
        j=0
        for i in range(len(self.coef)):
            j=(x**(self.grado-i))*self.coef[i] # 
            y=y+j
        return y                                    ## se devielve el valor resultante de evaliar y sumar 

## funciones 

def capturar_poli():                                                ## funcion para capturar los datos del polinomio que desea el usuario.                       
    bandera=1                                                       ## condicion para ingresar al while
    print('Ingrese los datos del polinomio.')
    while bandera!=0:
        try:                                                        ## caso ideal o donde se ingresan los datos correctos
            grado=int(input('Grado del polinomio.'))
            bandera=0
        except ValueError:                                          ## caso para cuando hay un dato que no es entero
            print('Por favor ingrese un numero entero.')
            bandera=1        
    
    coeficientes=np.zeros(grado+1)                                  ## creacion del vector que contendra los coeficientes
   
    for i in range(len(coeficientes)):
        bandera2=1                                                  ## condicion para ingresar al while
    
        while bandera2!=0:
             try:                                                   ## caso ideal o donde se ingresan los datos correctos
                 coeficientes[i]=float(input('Ingrese el coeficiente a({}) del polinomio.'.format(grado-i)))
                 bandera2=0
             except ValueError:                                     ## caso para cuando hay un dato que no es un numero
                    print('Por favor ingrese un numero.')
                    bandera2=1
    return Polinomio(grado, coeficientes)                           ## se devuelve el polinomio ingresado por el usuario.

def confirmacion(opc):
    a=['sumar','resta','multiplicar','multiplicar por un escalar','evaluar un polinomio']
    print('Usted escogió la opción {}, desea continuar con la operación [S/N]'.format(a[opc-1]))
    cont=input()
    if opc==2:
        print('El segundo polinomio que se ingrese sera el que porte el signo negativo')
    
    while cont!='S' and cont!='N' and cont!='s' and cont!='n':
        print('La opción no es correcta intente nuevamente') 
        cont=input()
    return cont

def mostrar_pol(pol):
    print('El resultado de la operacion es:')
    for i in range(len(pol.coef)):
        print('{}X^({}) '.format(pol.coef[i],pol.grado-i),end='')
## captura de datos

print('Los polinomios que son la suma de un numero finitos de términos están definidos de la forma a(n)X^(n)+ a(n-1)X^(n-1)+ a(n-2)X^(n-2)+….+ a(2)X^(2)+ a(1)X^(1)+ a(0)X^(0). Donde a es el coeficiente del termino y n el máximo exponente que tendrá el polinomio, esto es conocido como grado del polinomio.')
print('¿Qué operación desea realizar? \n1. Sumar. \n2. Resta. \n3. Multiplicar. \n4. Multiplicar por un escalar. \n5. Evaluar un polinomio.\n6. Salir')
opc=input()
while opc!='1' and opc!='2' and opc!='3' and opc!='4' and opc!='5' and opc!='6':
   print('La opción no es correcta intente nuevamente') 
   opc=input()


## cuerpo

if opc=='1' or opc=='2':
    
        
    
    cont=confirmacion(int(opc))
        
    if cont=='S' or cont=='s':
        pol1=capturar_poli()
        pol2=capturar_poli()
        pol3=pol1.suma_resta(pol2, int(opc))
        mostrar_pol(pol3)
        
# if opc==3:
    
# if opc==4:
    
# if opc==5:

