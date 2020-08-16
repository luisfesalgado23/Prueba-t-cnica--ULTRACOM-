# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 09:55:54 2020

@author: Usuario
"""

import numpy as np
    
class Polinomio:
    def __init__(self,grado,coef):
        self.grado=grado
        self.coef=coef
        
    def suma_resta(self,pol2,op):
         ## la resta se hace recibiendo un objeto de tipo polinomio el cual sera el portador del signo negativo en la operacion
        ## op sera laopcion de ser una suma si vale 1 una resta en cualquier otro caso
        
        if pol2.grado>self.grado:  ## encontrando el polinomio con el mayor grado
           may=pol2.grado
           men=self.grado
           coef_may=pol2.coef
           coef_men=self.coef
           if op==1:
               smay=1                       ## signo que tiene el polinomio mayor
               smen=1                      ## signo que tiene el polinomio menor
           else:
               smay=-1                       ## signo que tiene el polinomio mayor
               smen=1                      ## signo que tiene el polinomio menor
        
        else :#: ## encontrando el polinomio con el mayor grado
           men=pol2.grado
           may=self.grado
           coef_men=pol2.coef
           coef_may=self.coef
           if op==1:
               smay=1                       ## signo que tiene el polinomio mayor
               smen=1                      ## signo que tiene el polinomio menor
           else:
               smay=1                       ## signo que tiene el polinomio mayor
               smen=-1                      ## signo que tiene el polinomio menor
                   
        new_coef=np.zeros(may)
        for i in range(may):
            if i>=men:
               new_coef[may-i-1]=coef_may[may-i-1]*smay   ##rellenar los coeficientes que no tienen con quien restarse por tener un grado mayor al de otro polinomio
            else:
               new_coef[may-i-1]=coef_may[may-i-1]*smay+coef_men[men-i-1]*smen  ##resta de los coeficientes del mismo grado
        return Polinomio(may, new_coef)
 
    
 ##   def mult_poli(self,pol2):
        
 ##   def mult_esca(self,esc):
        
 ##   def evaluar(self,x):
        
d=[1,4,6,8,4,3,2,1,2,2]
c=[3,2,1,2,2]
u=[1,2,3,4,5]
ga=10
gb=5
gc=5
pol1=Polinomio(ga,d)
pol2=Polinomio(gb,c)
pol5=Polinomio(gc,u)


pol3=pol1.suma_resta(pol2,1)
pol7=pol2.suma_resta(pol1,1)
pol4=pol2.suma_resta(pol1,2)
pol8=pol1.suma_resta(pol2,2)
pol6=pol5.suma_resta(pol2,1)
pol9=pol2.suma_resta(pol5,2)
