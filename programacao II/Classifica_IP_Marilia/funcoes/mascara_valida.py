#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mascara_valida.py
#
#  Marilia Ribeiro da Silva <marilia.ifc@gmail.com>

def valida_mascara(mascara):
    '''
    Recebe como parâmetro a máscara do IP em inteiro e retorna o que
    estiver etre 8 e 32.

    >>> valida_mascara(2)
    False
    >>> valida_mascara(8)
    True
    >>> valida_mascara(24)
    True
    >>> valida_mascara(32)
    True
    >>> valida_mascara(34)
    False
    '''
    return mascara >= 8 and mascara <= 32

if __name__ == "__main__":
    import doctest
    doctest.testmod()
