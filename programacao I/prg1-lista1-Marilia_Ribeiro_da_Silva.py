#!/bin/env python3
# coding: utf-8
# Marilia Ribeiro da Silva <marilia.ifc@gmail.com>
# Lista de exercícios 1

def soma_dois_inteiros(numero_inteiro1,numero_inteiro2):
    ''' Recebe dois numeros inteiros, e retorna a sua soma'''
    soma = numero_inteiro1 + numero_inteiro2
    return soma

def metro_para_milimetros(metros):
    ''' Recebe um valor em metros, e retorna o valor em milimetros'''
    milimetros = metros * 1000
    return milimetros

def dias_para_segundos(dias,horas,minutos,segundos):
    ''' Recebe uma data em dias com horas,minutos,segundos, e retorna 
    a data em segundos'''
    tempo = float((dias * 86400) + (horas * 3600) + (minutos * 60) + segundos)
    return tempo

def aumento_salarial(salario,porcentagem):
    ''' Recebe um salario e sua porcentagem de aumento, e retorna
    o novo salario'''
    novo_salario = salario + (salario * (porcentagem/100))
    return round(novo_salario,2)

def preco_com_desconto(preco,desconto):
    ''' Recebe um preço e sua porcentagem de desconto, e retorna 
    novo preço'''
    novo_preco = float(preco - (preco*(desconto/100)))
    return round(novo_preco,2)

def tempo_para_percorrer_uma_distancia(distancia,velocidade):
    ''' Recebe uma distancia e a velocidade que percorreras essa 
    distancia, e retorna as horas que seriam gastas para percorrer
     em linha reta'''
    tempo_horas = float(distancia / velocidade) #horas
    return round(tempo_horas,2)

def celsius_para_fahrenheit(celsius):
    ''' Recebe uma temperatura em celsius, e retorna a temperatura 
    em fahrenheit'''
    temperatura = (celsius * 1.8) + 32
    return temperatura

def fahrenheit_para_celsius(fahrenheit):
    ''' Recebe uma temperatura em fahrenheit, e retorna a temperatura
      celcius'''
    temperatura = (fahrenheit - 32)/1.8
    return round(temperatura, 2)

def preco_aluguel_carro(dias,km):
    ''' Recebe uma quantidade de dias que o carro foi alugado e a 
    quantidade de kilometros rodados, e retorna o valor a ser pago'''
    taxa_dia = 60.00
    taxa_km = 0.15
    preco = (taxa_dia * dias) + (taxa_km * km)
    return preco

def dias_perdidos_por_fumar(cigarros,anos):
    ''' Recebe uma quantidade de cigarros fumados por dia e a quantidade
     de anos que fuma, e retorna o total de dias perdidos'''
    minutos_cigarro = 10 #minutos
    dias = (((anos * 365) * (cigarros * minutos_cigarro))/1440)
    return round(dias,2)

def dois_elevado_a_um_milhao():
    ''' Calcula dois elevado a um milhão, e retorna a quantidade de 
    algarismos'''
    quantidade_numeros = (len(str(2**1000000)))
    return quantidade_numeros

# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0 

def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = ' Falhou.'
    else:
        prefixo = ' Passou.'
        acertos += 1
    print ('%s Esperado: %s \tObtido: %s' % (prefixo, repr(esperado), 
        repr(obtido)))

def main():
    print('Soma dois inteiros:')
    test(soma_dois_inteiros(0,0), 0) 
    test(soma_dois_inteiros(-1,0), -1) 
    test(soma_dois_inteiros(1,1), 2) 
    test(soma_dois_inteiros(0,-1), -1) 

    print('Metros para milimetros:')
    test(metro_para_milimetros(0), 0) 
    test(metro_para_milimetros(1), 1000) 
    test(metro_para_milimetros(1.8), 1800) 
    test(metro_para_milimetros(1.81), 1810) 

    print('Dias,horas,minutos e segundos para segundos:')
    test(dias_para_segundos(10,20,59,1), 939541)
    test(dias_para_segundos(0,23,59,59), 86399)
    test(dias_para_segundos(1,1,1,1), 90061)
    test(dias_para_segundos(1,0,0,0), 86400)

    print('Aumento salarial baseado na porcentagem de aumento:')
    test(aumento_salarial(1330,20), 1596.00)
    test(aumento_salarial(1000,0), 1000.00)
    test(aumento_salarial(1000.10,123), 2230.22)
    test(aumento_salarial(0.0,200), 0.00)

    print('Desconto do preco atual baseado na porcentagem do desconto:')
    test(preco_com_desconto(1330,20), 1064.00)
    test(preco_com_desconto(1000,0), 1000.00)
    test(preco_com_desconto(1000.10,5.5), 945.09)
    test(preco_com_desconto(0.0,200), 0.00)

    print('Tempo gasto para percorrer um distancia a uma velocidade'
    'constante(linha reta):')
    test(tempo_para_percorrer_uma_distancia(1330,20), 66.50)
    test(tempo_para_percorrer_uma_distancia(1000,100), 10.00)
    test(tempo_para_percorrer_uma_distancia(1000,123), 8.13)
    test(tempo_para_percorrer_uma_distancia(100000,201), 497.51)

    print('Celsius para Fahrenheit:')
    test(celsius_para_fahrenheit(30), 86.00)
    test(celsius_para_fahrenheit(300), 572.00)
    test(celsius_para_fahrenheit(-100), -148.00)
    test(celsius_para_fahrenheit(1), 33.80)

    print('Fahrenheit para Celsius:')
    test(fahrenheit_para_celsius(30), -1.11)
    test(fahrenheit_para_celsius(300), 148.89)
    test(fahrenheit_para_celsius(-100), -73.33)
    test(fahrenheit_para_celsius(1), -17.22)

    print('Preco a pagar pelo aluguel do carro:')
    test(preco_aluguel_carro(10,100), 615.00)
    test(preco_aluguel_carro(13,133), 799.95)
    test(preco_aluguel_carro(1,0), 60.00)
    test(preco_aluguel_carro(3,79), 191.85)

    print('Total de dias que perdeu de viver por ter fumados:')
    test(dias_perdidos_por_fumar(10,10), 253.47)
    test(dias_perdidos_por_fumar(13,13), 428.37)
    test(dias_perdidos_por_fumar(0,110), 0.00)
    test(dias_perdidos_por_fumar(3,79), 600.73)

    print('Calcula a quantidade de numeros que ha em dois elevado a um'
    'milhao:')
    test(dois_elevado_a_um_milhao(), 301030)

if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" %(total, acertos,
     total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
