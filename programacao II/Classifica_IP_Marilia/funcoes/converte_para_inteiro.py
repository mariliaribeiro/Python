#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  converte_para_inteiro.py
#
#  Marilia Ribeiro da Silva <marilia.ifc@gmail.com>

def converte_para_inteiro(ip):
    '''
    Revebe como parâmetro um IP em binário e converte para decimal.

    >>> converte_para_inteiro('11000000.10101000.00000010.00000000')
    '192.168.2.0'
    '''

    ip = ip.split('.')
    return '.'.join([str(int(bit,2)) for i, bit in enumerate(ip)])

if __name__ == "__main__":
    import doctest
    doctest.testmod()
