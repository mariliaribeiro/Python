#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# print_informacoes_ip_mascara.py
#
#  Marilia Ribeiro da Silva <marilia.ifc@gmail.com>


from funcoes.classifica_ip import *
from funcoes.informacoes_mascara import *
from funcoes.subrede_broadcast import *
from funcoes.converte_mascara_32bits import *
from funcoes.converte_mascara_4bytes import *


def informacoes_ip_mascara(ip, mascara):
    #desempacota informações a serem informadas ao usuário
    ip_bin, classe, rede, host = classifica_ip(ip) # informações do IP

    ips_validos, hosts, sub_redes, saltos, qtd_uns, qtd_zeros = informacoes_mascara(mascara) # informações da máscara

    ip_rede, ip_broadcast, ip_rede_int, ip_broadcast_int = (subrede_broadcast(mascara, ip)) # informações da máscara

    #conversão da máscara
    mascara_32bits = converte_mascara_32bits(mascara)
    mascara_4bytes = converte_mascara_4bytes(mascara)

    #imprime os dados na tela
    return('IP Decimal: %s \n'
          'IP Binário: %s \n'
          'Classe: %s \n'
          'Rede: %s     '
          'Host: %s \n'
          '----\n'
          'Máscara: %s = %s = %s \n'
          'IP de Rede: %s/%s = %s/%s \n'
          'IP de Broadcast: %s/%s = %s/%s \n'
          'IPs válidos: %s     '
          'Hosts: %s    '
          'Sub-redes: %s'
          %(ip, ip_bin, classe, rede, host, mascara_32bits, mascara_4bytes, mascara, ip_rede,
          mascara, ip_rede_int, mascara, ip_broadcast, mascara, ip_broadcast_int, mascara, ips_validos, hosts, sub_redes))
