#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  converte_para_binario.py
#
#  Marilia Ribeiro da Silva <marilia.ifc@gmail.com>

def converte_para_binario(ip):
    '''
    Recebe como parâmetro um IP em decimal e devolve o IP em binário
    >>> converte_para_binario('1.128.0.0')
    '00000001.10000000.00000000.00000000'
    >>> converte_para_binario('128.128.0.0')
    '10000000.10000000.00000000.00000000'
    >>> converte_para_binario('192.128.0.0')
    '11000000.10000000.00000000.00000000'
    >>> converte_para_binario('224.128.0.0')
    '11100000.10000000.00000000.00000000'
    >>> converte_para_binario('255.128.0.0')
    '11111111.10000000.00000000.00000000'
    '''

    ip = ip.split('.')
    binario = ''
    for bit in range(len(ip)):
        if bit < 3:
            binario += ('{:08b}'.format(int(ip[bit]))) + '.'
        else:
            binario += ('{:08b}'.format(int(ip[bit])))
    return binario

if __name__ == "__main__":
    import doctest
    doctest.testmod()
