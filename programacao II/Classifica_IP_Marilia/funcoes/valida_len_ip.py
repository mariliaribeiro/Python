#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  valida_len_ip.py
#
#  Marilia Ribeiro da Silva <marilia.ifc@gmail.com>


def valida_len_ip(list_ip):
    '''
    Recebe como parâmetro uma lista com as partes do IP e retorna o IP que
    tiver tamanho igual a 4.

    >>> valida_len_ip(['1', '128', '0', '0'])
    True
    >>> valida_len_ip(['128', '128'])
    False
    >>> valida_len_ip(['192', '128', '0', '0', '0'])
    False
    '''
    return len(list_ip) == 4

if __name__ == "__main__":
    import doctest
    doctest.testmod()
