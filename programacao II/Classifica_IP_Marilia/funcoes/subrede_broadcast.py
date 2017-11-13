#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# subrede_broadcast.py
#
#  Marilia Ribeiro da Silva <marilia.ifc@gmail.com

from funcoes.informacoes_mascara import *
from funcoes.limpa_string import *
from funcoes.converte_mascara_32bits import *
from funcoes.converte_para_binario import *
from funcoes.converte_para_inteiro import *

def subrede_broadcast(mascara, ip):
    '''
    Recebe como parâmetros a máscara em inteiro e o IP e retorna o IP da
    rede e o IP de broadcast.

    >>> subrede_broadcast(27, '192.168.2.2')
    ('11000000.10101000.00000010.00000000', '11000000.10101000.00000010.00011111', '192.168.2.0', '192.168.2.31')
    >>> subrede_broadcast(27, '192.168.120.123')
    ('11000000.10101000.01111000.01100000', '11000000.10101000.01111000.01111111', '192.168.120.96', '192.168.120.127')
    '''

    qtd_uns = (informacoes_mascara(mascara))[-2]
    mascaras = list(limpa_string(converte_mascara_32bits(mascara)))
    ips = list(limpa_string(converte_para_binario(ip)))
    rede = ''
    broadcast = ''

    for i in range(1,33):
        ip_int = int(ips[i-1])
        mascara_int = int(mascaras[i-1])
        if i <= qtd_uns:
            rede += (str(ip_int and mascara_int))
            broadcast += (str(ip_int and mascara_int))
        else:
            rede += '0'
            broadcast += '1'
        if i % 8 == 0 and i != 32:
            rede +='.'
            broadcast += '.'
    return rede, broadcast, converte_para_inteiro(rede), converte_para_inteiro(broadcast)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
