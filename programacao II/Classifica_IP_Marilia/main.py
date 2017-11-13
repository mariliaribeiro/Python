#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#
#  Marilia Ribeiro da Silva <marilia.ifc@gmail.com>

from funcoes.separa_ip_mascara import *
from funcoes.mascara_valida import *
from funcoes.ip_valido import *
from funcoes.print_informacoes_ip_mascara import *
from funcoes.compara_rede_host import *


def main():
    ips = [] # cria uma lista com os ips digitados
    mascaras = []

    for i in range(0,2):
        ip_masc = input(str('\n\n--> Digite o IP em decimal e sua máscara (10.0.0.0/8): '))

        #separa ip da mascara
        ip, mascara = separa_ip_mascara(ip_masc)

        if valida_mascara(mascara): #valida máscara
            if ip_valido(ip): #valida ip
                ips.append(ip) #add ip na lista ips
                mascaras.append(mascara)
                print(informacoes_ip_mascara(ip, mascara))
            else:
                print('Informe um IP válido')
        else:
            print('Informe uma máscara válida')


    # imprime a comparação de rede e host
    print('\n\n <----------------- Compara Rede e Host -----------------> \n' + compara_rede_host(ips))



if __name__ == '__main__':
    main()
