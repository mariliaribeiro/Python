#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  print_informacoes_ip.py
#
#  Marilia Ribeiro da Silva <marilia.ifc@gmail.com>

def separa_ip_mascara(ip_masc):
    '''
    Recebe como parâmetro um IP e uma máscara e retorna os dois separados.
    Caso seja informado apenas o IP, retorna uma mácara com valor 8.

    >>> separa_ip_mascara('1.1.1.1/24')
    ('1.1.1.1', 24)
    >>> separa_ip_mascara('1.1.1.1')
    ('1.1.1.1', 8)
    '''

    if '/' not in ip_masc:
        ip = ip_masc #.split('.')
        mascara = 8 #valor default
    else:
        separa = ip_masc.split('/')
        ip = str(separa[0])
        #ip = (separa[0]).split('.')
        mascara = int(separa[1])
    return ip, mascara


if __name__ == "__main__":
    import doctest
    doctest.testmod()
