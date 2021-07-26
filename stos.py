# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 00:33:31 2020

@author: arkad
"""

class Stos:
    pass

class Element:
    pass
def utworz_stos():
    stos = Stos()
    stos.wierzch = None
    return stos
def na_stos(stos, wartosc):

    elem = Element()
    elem.wartosc = wartosc
    elem.poprzedni = stos.wierzch
    stos.wierzch = elem
    
def ze_stosu(stos):
    if stos.wierzch is None:
        raise IndexError("Pusty stos")
        elem = stos.wierzch
        stos.wierzch = elem.p