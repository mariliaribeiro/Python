#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ip_decimal.py
#
#  Marilia Ribeiro da Silva <marilia.ifc@gmail.com>


def ip_decimal(bits_ip):
    '''
    Recebe como parâmetro um IP em binpario e devolve o IP em decimal
    >>> ip_decimal(['1', '128', '0', '0'])
    '1.128.0.0'
    >>> ip_decimal(['128', '128', '0', '0'])
    '128.128.0.0'
    >>> ip_decimal(['192', '128', '0', '0'])
    '192.128.0.0'
    >>> ip_decimal(['224', '128', '0', '0'])
    '224.128.0.0'
    >>> ip_decimal(['255', '128', '0', '0'])
    '255.128.0.0'
    '''
    ip_decimal = ''
    for i, bit in enumerate(bits_ip):
        if i < (len(bits_ip)-1):
            ip_decimal += bit + '.'
        else:
            ip_decimal += bit
    return ip_decimal

if __name__ == "__main__":
    import doctest
    doctest.testmod()
