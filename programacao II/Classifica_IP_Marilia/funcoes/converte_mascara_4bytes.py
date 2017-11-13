#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  converte_mascara_4bytes.py
#
#  Marilia Ribeiro da Silva <marilia.ifc@gmail.com>

from funcoes.converte_mascara_32bits import *
from funcoes.converte_para_inteiro import *

def converte_mascara_4bytes(mascara):
    '''
    Recebe como parâmetro a máscara  em número inteiro e converte para o formato de 4 bytes.

    >>> converte_mascara_4bytes(18)
    '255.255.192.0'
    '''

    mascaras = (converte_mascara_32bits(mascara))
    return converte_para_inteiro(mascaras)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
