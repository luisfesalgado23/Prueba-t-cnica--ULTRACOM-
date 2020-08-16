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
        ## op sera laopcion de ser una suma si vale 1 una resta en cualquier otro caso
        
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
        
        
        
d=[1,4,6,8,4,3,2,1,2,2]
c=[3,2,1,2,2]
u=[1,2,3,4,5]
t=[-2,2,-3,6]
q=[1,2,-1]
ga=10
gb=5
gc=4
pol1=Polinomio(ga,d)
pol2=Polinomio(gb,c)
pol5=Polinomio(gc,u)
x1=Polinomio(3, t)
x2=Polinomio(2, q)
x3=x1.mult_poli(x2)
pol3=pol1.suma_resta(pol2,1)
pol7=pol2.suma_resta(pol1,1)
pol4=pol2.suma_resta(pol1,2)
pol8=pol1.suma_resta(pol2,2)
pol6=pol5.suma_resta(pol2,1)
pol9=pol2.suma_resta(pol5,2)

p=pol5.evaluar(4)
pol19=pol1.mult_esca(0.5)
