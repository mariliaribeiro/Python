#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  valida_bit_ip.py
#
#  Marilia Ribeiro da Silva <marilia.ifc@gmail.com>


def valida_bit_ip(list_ip):
    '''
    Recebe como parâmetro uma lista com as partes do IP e retorna o bit
    que estiver entre 0 e 255.

    >>> valida_bit_ip(['1', '128', '0', '0'])
    True
    >>> valida_bit_ip(['256', '128', '0', '0'])
    False
    >>> valida_bit_ip(['256', '128', '0', ''])
    False
    >>> valida_bit_ip(['256', ' ', '0', '0'])
    False
    '''
    for bit in list_ip:
        if int(bit) < 0 or int(bit) > 255:
            return False
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
