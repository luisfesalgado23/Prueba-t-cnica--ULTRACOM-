# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np

class Pieza:
    def __init__(self,fila,columna,tipo):       ## atributos de las piezas del juego
        self.fila=fila                          ## fila en la que se encuentra ubicada
        self.columna=columna                    ## columna donde se encuentra ubicada
        self.tipo=tipo                          ## tipo de pieza entre las existentes en el ajedrez
        
    def movimiento(self,fila,columna):         ## función que realiza un cambio de posición en el tablero
        self.fila=fila
        self.columna=columna

