#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# limpa_string.py
#
#  Marilia Ribeiro da Silva <marilia.ifc@gmail.com


def limpa_string(lista):
    '''
    Recebe como parâmetro uma lista contendo a máscara no formato de 32 bits
    e retorna apenas os números.

    >>> limpa_string(['1', '1', '1', '1', '1', '1', '1', '1', '.', '1', '1', '1', '1', '1', '1', '1', '1', '.', '1', '1', '0', '0', '0', '0', '0', '0', '.', '0', '0', '0', '0', '0', '0', '0', '0'])
    '11111111111111111100000000000000'
    '''
    import string
    return ''.join([caracter for caracter in lista if caracter in string.digits])

if __name__ == "__main__":
    import doctest
    doctest.testmod()
