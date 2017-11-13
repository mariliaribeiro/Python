#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  compara_rede_host.py
#
#  Marilia Ribeiro da Silva <marilia.ifc@gmail.com>


from funcoes.classifica_ip import *

def compara_rede_host(ips):
    '''
    Recebe como parâmetro uma lista contendo dois IPs e devolve uma comparação entre a rede e o host.
    >>> compara_rede_host(['1.128.0.0', '1.228.0.1'])
    'Os IPs 1.128.0.0 e 1.228.0.1 pertencem a mesma rede (1) e aos hosts 128.0.0 e 228.0.1, respectivamente.'
    >>> compara_rede_host(['192.128.0.0', '128.128.0.0'])
    'Os IPs 192.128.0.0 e 128.128.0.0 pertencem as redes 192.128.0 e 128.128, respectivamente e aos hosts 0 e 0.0, respectivamente.'
    >>> compara_rede_host(['224.128.0.0', '255.128.0.0'])
    'Os IPs 224.128.0.0 e 255.128.0.0 pertencem as redes 224.128.0.0 e 255.128.0.0, respectivamente e ao mesmo host ().'
    >>> compara_rede_host(['192.168.0.0', '192.168.0.0'])
    'Os IPs 192.168.0.0 e 192.168.0.0 pertencem a mesma rede (192.168.0) e ao mesmo host (0).'
    >>> compara_rede_host(['192.168.0.0'])
    'Informe pelo menos dois IPs para efetuar a comparação de rede e host.'
    >>> compara_rede_host([])
    'Informe pelo menos dois IPs para efetuar a comparação de rede e host.'
    '''
    redes = []
    hosts = []
    rede = ''
    host = ''
    

    if len(ips) >= 2:
        for i, ip in enumerate(ips):
            info = classifica_ip(ip)
            redes.append(info[2])
            hosts.append(info[3])
			
            if i > 0:
                for i, r in enumerate(redes):
                    if redes[i-1] == redes[i]:
                        rede = ('a mesma rede (%s)' %(redes[i]))
                    else:
                        rede = ('as redes %s e %s, respectivamente' %(redes[i-1], redes[i]))

                for i, h in enumerate(hosts):
                    if hosts[i-1] == hosts[i]:
                        host = ('ao mesmo host (%s).' %(hosts[i]))
                    else:
                        host = ('aos hosts %s e %s, respectivamente.' %(hosts[i-1], hosts[i]))
                return ('Os IPs %s e %s pertencem %s e %s' %(ips[i-1], ips[i], rede, host))
    else:
        return ('Informe pelo menos dois IPs para efetuar a comparação de rede e host.')



if __name__ == "__main__":
    import doctest
    doctest.testmod()
