#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# multiplos_oito.py
#
#  Marilia Ribeiro da Silva <marilia.ifc@gmail.com>

def multiplos_oito(qtd_uns):
    '''
    Recebe como parâmetro a quantidade de uns existentes na mácara de
    32 bits e retorna a quantidade de uns no byte misto.

    >>> multiplos_oito(18)
    2
    >>> multiplos_oito(16)
    0
    >>> multiplos_oito(27)
    3
    '''
    multiplos = [8, 16, 24, 32]
    for multiplo in multiplos:
        if qtd_uns >= multiplo:
            qtd_uns_byte_misto = abs(qtd_uns - multiplo)
    return qtd_uns_byte_misto

if __name__ == "__main__":
    import doctest
    doctest.testmod()
