#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  converte_mascara_32bits.py
#
#  Marilia Ribeiro da Silva <marilia.ifc@gmail.com>

def converte_mascara_32bits(mascara):
    '''
    Recebe como parâmetro a mácara em número inteiro e transforma para 32 bits.

    >>> converte_mascara_32bits(18)
    '11111111.11111111.11000000.00000000'
    '''
    #mascara_decial = ''.join(['1' if i <= mascara else '0' for i in range(1,33)])
    mascara_decimal = ''
    for i in range(1,33):
        if i <= mascara:
            mascara_decimal += '1'
        else:
            mascara_decimal += '0'
        if i % 8 == 0 and i != 32:
            mascara_decimal +='.'
    return mascara_decimal


if __name__ == "__main__":
    import doctest
    doctest.testmod()
