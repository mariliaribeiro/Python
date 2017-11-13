#!/usr/bin/env python3
#coding: utf-8
# Marilia Ribeiro da Silva
# Assunto: prg2-Surf-Marilia_Ribeiro_da_Silva

# criar discionario com chave == nota
arquivo = open('surf.txt')
notas = {}
for linha in arquivo:
    nome, pontos = linha.split()
    notas[nome] = float(pontos)
arquivo.close()


def ordena_tupla(tupla):
    return tupla[1]
    
notas = list(notas.items())
for nome, nota in sorted(notas, key = ordena_tupla, reverse = True):
    print('%10s: %4.2f' %(nome, nota))
