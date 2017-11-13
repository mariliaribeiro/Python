#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  informacoes_ip.py
#
#  Marilia Ribeiro da Silva <marilia.ifc@gmail.com>

from funcoes.converte_para_binario import *
from funcoes.ip_decimal import *
from funcoes.separa_ip_mascara import *

def classifica_ip(ip):
    '''
    Recebe como parâmetro um IP e devolve:
    - a classe
    - o IP em binário
    - a rede
    - o host

    Classe A: bit[0] == 0 (zero)
    Classe B: bit[:1] == 10 (um, zero)
    Classe C: bit[:2] == 110 (um, um, zero)
    Classe D: bit[:3] == 1110 (um, um, um, zero) - (endereço multicast)
    Classe E: bit[:3] == 1111 (um, um, um, um) - (endereço especial reservado)

    >>> classifica_ip('1.128.0.0')
    ('00000001.10000000.00000000.00000000', 'A', '1', '128.0.0')
    >>> classifica_ip('128.128.0.0')
    ('10000000.10000000.00000000.00000000', 'B', '128.128', '0.0')
    >>> classifica_ip('192.128.0.0')
    ('11000000.10000000.00000000.00000000', 'C', '192.128.0', '0')
    >>> classifica_ip('224.128.0.0')
    ('11100000.10000000.00000000.00000000', 'D', '224.128.0.0', '')
    >>> classifica_ip('255.128.0.0')
    ('11111111.10000000.00000000.00000000', 'E', '255.128.0.0', '')
    '''
    ip_bin = converte_para_binario(ip)
    bits_ip = ip.split('.')
    #bits_ip = ip
    classe = ''
    rede = ''
    host = ''

    if '0' in ip_bin[0]:
        classe = 'A'
        rede = ip_decimal(bits_ip[0])
        host = ip_decimal(bits_ip[1:])
    elif '10' in ip_bin[:2]:
        classe = 'B'
        rede = ip_decimal(bits_ip[:2])
        host = ip_decimal(bits_ip[2:])
    elif '110' in ip_bin[:3]:
        classe = 'C'
        rede = ip_decimal(bits_ip[:3])
        host = ip_decimal(bits_ip[3:])
    elif '1110' in ip_bin[:4]:
        classe = 'D'
        rede = ip_decimal(bits_ip)
    elif '1111' in ip_bin[:4]:
        classe = 'E'
        rede = ip_decimal(bits_ip)
    return (ip_bin, classe, rede, host)
    #return ('IP Decimal: %s    IP Binário: %s \nClasse: %s    Rede: %s    Host: %s    ' %(ip, ip_bin, classe, rede, host))

def print_info(ip):
    informacoes_ip = classifica_ip(ip)
    for ip_bin, classe, rede, host in informacoes_ip:
        print (ip_bin, classe, rede, host)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print_info('1.1.1.1')
