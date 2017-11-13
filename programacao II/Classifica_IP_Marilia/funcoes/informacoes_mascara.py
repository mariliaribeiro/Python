#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# informacoes_mascara.py
#
#  Marilia Ribeiro da Silva <marilia.ifc@gmail.com>

from funcoes.converte_mascara_32bits import *
from funcoes.multiplos_oito import *

def informacoes_mascara(mascara):
    '''
    Recebe como parâmetro a maścara em número inteiro e retorna as seguintes informações:
    - quantidade de IPs válidos
    - quantidade de hosts
    - quantidade de sub-redes
    - saltos entre cada sub-rede
    - quantidade de 1 na máscara de 32 bits
    - quantidade de 0 na máscara de 32 bits

    >>> informacoes_mascara(18)
    (16384, 16382, 4, 16383, 18, 14)
    >>> informacoes_mascara(24)
    (256, 254, 0, 255, 24, 8)
    >>> informacoes_mascara(27)
    (32, 30, 8, 31, 27, 5)
    '''

    mascaras = list(converte_mascara_32bits(mascara))
    qtd_zeros = (mascaras.count('0'))
    qtd_uns = (mascaras.count('1'))

    qtd_uns_byte_misto = multiplos_oito(qtd_uns)
    #if qtd_uns_byte_misto == 0:
    #    qtd_sub_redes = 0
    #else:
    qtd_sub_redes = int(2** qtd_uns_byte_misto) #conta 1 do misto


    qtd_ips_validos = 2** qtd_zeros #0 de tudo == ip_valido
    qtd_host = abs((2** qtd_zeros)-2)

    saltos = abs((2** qtd_zeros) - 1)

    return qtd_ips_validos, qtd_host, qtd_sub_redes, saltos, qtd_uns, qtd_zeros


if __name__ == "__main__":
    import doctest
    doctest.testmod()
