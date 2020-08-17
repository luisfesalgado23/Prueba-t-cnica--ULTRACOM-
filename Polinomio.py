# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 09:55:54 2020

@author: Luis Fernando Salgado
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
           if op==1:                        ## condicion para la suma
               smay=1                       ## signo que tiene el polinomio mayor
               smen=1                      ## signo que tiene el polinomio menor
           else:                            ## condicion para la resta
               smay=-1                       ## signo que tiene el polinomio mayor
               smen=1                      ## signo que tiene el polinomio menor
        
        else :#: ## encontrando el polinomio con el mayor grado
           men=len(pol2.coef)
           may=len(self.coef)
           coef_men=pol2.coef
           coef_may=self.coef
           if op==1:                        ## condicion para la suma
               smay=1                       ## signo que tiene el polinomio mayor
               smen=1                      ## signo que tiene el polinomio menor
           else:                            ## condicion para la resta
               smay=1                       ## signo que tiene el polinomio mayor
               smen=-1                      ## signo que tiene el polinomio menor
                   
        new_coef=np.zeros(may)              ## variabe para guardar los resultados de la operacion.
        for i in range(may):
            if i>=men:
               new_coef[may-i-1]=coef_may[may-i-1]*smay   ##rellenar los coeficientes que no tienen con quien restarse o sumarse  por tener un grado mayor al de otro polinomio
            else:
               new_coef[may-i-1]=coef_may[may-i-1]*smay+coef_men[men-i-1]*smen  ##resta o suma de los coeficientes del mismo grado
        return Polinomio(may-1, new_coef)     ## se devuelve un polimo que es el resultado de la operacion seleccionada
 
    
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
            j=(x**(self.grado-i))*self.coef[i] #        ## se eleva x con su correspondiente exponente y se multiplica por el coeficiente
            y=y+j                                           ## acumulacion de resultados
        return y                                    ## se devielve el valor resultante de evaliar y sumar 

## funciones 

def capturar_poli():                                                ## funcion para capturar los datos del polinomio que desea el usuario.                       
    bandera=1                                                       ## condicion para ingresar al while
    
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

def confirmacion(opc):                                              ## valida que el usuario no haya escogido otra opcion por equivocacion por ejemplo suma en vez de resta
    a=['sumar','resta','multiplicar','multiplicar por un escalar','evaluar un polinomio']
    print('Usted escogió la opción {}, desea continuar con la operación [S/N]'.format(a[opc-1]))
    cont=input()
    if opc==2 and cont!='N' and cont!='n':                          ## condicion especial para la resta
        print('El segundo polinomio que se ingrese sera el que porte el signo negativo')
    
    while cont!='S' and cont!='N' and cont!='s' and cont!='n':          ## validar datos correctos
        print('La opción no es correcta intente nuevamente') 
        cont=input()
    return cont

def mostrar_pol(pol):                               ## funcion para imprimir de manera ordenada los datos
    print('\nEl resultado de la operacion es:')
    for i in range(len(pol.coef)):
        if i==0:                                    ## no se muestra el signo positivo del primer termino
            print('{}X^({}) '.format(pol.coef[i],pol.grado-i),end='')
        if i==pol.grado:
             print('{:+}'.format(pol.coef[i]))
        if i>0 and i<pol.grado:
            print('{:+}X^({}) '.format(pol.coef[i],pol.grado-i),end='') ## no se muestra la X en el termino independiente
        
def captura_esc(opc):
    bandera2=1                                                  ## condicion para ingresar al while
    
    while bandera2!=0:
         try:                                                   ## caso ideal o donde se ingresan los datos correctos
            if opc==5:
                esc=float(input('Ingrese el valor de X con el que desea evaluar el polinomio'))  ## Semuestra para cuando se evalua el polinomio
                 
            else:
                 esc=float(input('Ingrese el valor del escalar con el que desea multiplicar el polinomio')) ## Semuestra para cuando se multiplica por un escalar el polinomio
            bandera2=0
         except ValueError:                                     ## caso para cuando hay un dato que no es un numero
                    print('Por favor ingrese un numero.')
                    bandera2=1
    return esc 


## cuerpo

print('Los polinomios que son la suma de un numero finitos de términos están definidos de la forma a(n)X^(n)+ a(n-1)X^(n-1)+ a(n-2)X^(n-2)+….+ a(2)X^(2)+ a(1)X^(1)+ a(0)X^(0). Donde a es el coeficiente del termino y n el máximo exponente que tendrá el polinomio, esto es conocido como grado del polinomio.')
opc='0'

while opc!='6':

    print('\n\n¿Qué operación desea realizar? \n1. Sumar. \n2. Resta. \n3. Multiplicar. \n4. Multiplicar por un escalar. \n5. Evaluar un polinomio.\n6. Salir')
    opc=input()
    while opc!='1' and opc!='2' and opc!='3' and opc!='4' and opc!='5' and opc!='6':
        print('La opción no es correcta intente nuevamente') 
        opc=input()

    if opc=='1' or opc=='2':            ## suma y resta de polinomios
    
        cont=confirmacion(int(opc))     ## confirmar que sea la operacion deseada
        
        if cont=='S' or cont=='s':  
            print('\nIngrese los datos del primer polinomio.')
            pol1=capturar_poli()
            print('\nIngrese los datos del segundo polinomio.')
            pol2=capturar_poli()
            pol3=pol1.suma_resta(pol2, int(opc))        ## llamar la funcion para sumar o restar
            mostrar_pol(pol3)
        
    if opc=='3':                    ##multiplicacion de polinomios
    
        cont=confirmacion(int(opc))
        
        if cont=='S' or cont=='s':
            print('\nIngrese los datos del polinomio.')
            pol1=capturar_poli()
            print('\nIngrese los datos del polinomio.')
            pol2=capturar_poli()
            pol3=pol1.mult_poli(pol2)       ## llamar la funcion para multiplicar
            mostrar_pol(pol3)
    
    if opc=='4':                    ##multiplicacion de polinomio por escalar
    
        cont=confirmacion(int(opc))
        
        if cont=='S' or cont=='s':
            print('\nIngrese los datos del polinomio.')
            pol1=capturar_poli()
            esc=captura_esc(opc)
            pol3=pol1.mult_esca(esc) ## llamar la funcion para multiplicar por un escalar
            mostrar_pol(pol3)
    
    if opc=='5':                ## evaluar el polinomio
    
        cont=confirmacion(int(opc))
        
        if cont=='S' or cont=='s':
            print('\nIngrese los datos del polinomio.')
            pol1=capturar_poli()
            esc=captura_esc(opc)
            resultado=pol1.evaluar(esc)                 ## llamar la funcion para evaluar
            print('El resultado de la operacion es: {}'.format(resultado))

