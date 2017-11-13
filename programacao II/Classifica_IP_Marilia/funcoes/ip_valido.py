#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ip_valido.py
#
#  Marilia Ribeiro da Silva <marilia.ifc@gmail.com>


from funcoes.valida_len_ip import *
from funcoes.valida_bit_ip import *

def ip_valido(ip):
    '''
    Recebe como parâmetro um IP em decimal e verifica se é válido.
    Para um IP ser válido deve ser composto por 4 valores (Ex. 10.10.1.0),
    sendo que cada valor deve estar entre 0 e 255.

    >>> ip_valido('1.128.0.0')
    True
    >>> ip_valido('128.128')
    False
    >>> ip_valido('192.128.0.0.0')
    False
    >>> ip_valido('256.128.0.0')
    False
    >>> ip_valido('257.256.258.254')
    False
    '''

    list_ip = ip.split('.')
    return valida_len_ip(list_ip)==True and valida_bit_ip(list_ip)==True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
