#!/bin/env python3
# coding: utf-8
# Marilia Ribeiro da Silva <marilia.ifc@gmail.com>
# Lista de exercícios 4b

# Exercícios sem for, apenas com while e sem funções embutidas.
# Você pode utilizar funções já desenvolvidas em outros exercícios

# -------- Funções a serem usadas -------- #
def media(lista):
    soma = 0
    i = 0 
    while i < len(lista):
        soma += lista[i]
        i += 1
    media = soma/len(lista)
    return media

def maior_menor(lista):
    maior = lista[0]
    menor = lista[0]
    i = 0
    while i < len(lista):
        if maior < lista[i]:
             maior = lista[i]
        else:
            menor = lista[i]
        i +=1
    return (maior, menor)


def primo(valor):
    i = 2
    if valor == 0 or valor == 1:
        return False
    else:
        while i < valor:
            if valor % i == 0:
                return False
            else:
                i += 1
        return True
        

# -------- Lista 4b -------- #
def media_anual(temperaturas):
    '''Receba uma lista com as temperaturas médias de cada mês
    e devolva uma lista com os números correspondentes aos meses que 
    possuem temperatura superior á média anual.'''
    
    temperaturas_superior_media_ano = []
    media_ano = media(temperaturas)   
    meses = len(temperaturas)
    i = 0 
    while i < meses:
        if temperaturas[i] > media_ano:
            temperaturas_superior_media_ano.append(i)
        i += 1        
    return temperaturas_superior_media_ano


def maiores_13(idades,alturas):
    '''Esta função recebe as idades e alturas de diversas pessoas, em duas
    listas separadas e de igual comprimento.
    Calcule a media das alturas e retorne as alturas daqueles que possuem 
    'idades' maior que 13 e altura inferior a media da turma'''
    i  = 0
    nova_lista = []
    media_altura = media(alturas)
    while i < len(idades):
        if idades[i] > 13 and alturas[i] < media_altura:
            nova_lista.append(alturas[i])
        i += 1
    return nova_lista

def media_saltos_lista(saltos):
    '''Receba uma lista com os saltos de um atleta e calcule a média dos 
    seus saltos, sabendo que o melhor e o pior saltos são desconsiderados.'''
    i = 0
    tamanho_lista = len(saltos)
    soma_saltos = 0
    maior = saltos[0]
    menor = saltos[0]
    while i < tamanho_lista:
        soma_saltos += saltos[i]
        if maior < saltos[i]:
            maior = saltos[i]
        if menor > saltos[i]:
            menor = saltos[i]
        i += 1       
    media_saltos = ((soma_saltos - (maior + menor))/(tamanho_lista -2))
    return round(media_saltos,1)
    
def lista_de_primos(inicio,fim):
    '''Retorne uma lista de primos entre os valores informados, incluindo
    os limites'''
    lista_primos=[]
    i = inicio
    while inicio <= fim:
        if primo(i) == True:
            lista_primos.append(i)
        fim -= 1
        i += 1
    return lista_primos
    
def Fibonacci(n):
    ''' Retorne uma lista com os n primeiros valores da série de Fibonacci.
    Fibonacci = 1,1,2,3,5,8,13,...''' 
    i = 0
    anterior = 1
    final_Fibonacci = 0
    lista_fibonacci = []
    while i < n:
        armazena = final_Fibonacci
        final_Fibonacci = final_Fibonacci + anterior
        anterior = armazena
        #print(armazena, final_Fibonacci, anterior)
        lista_fibonacci.append(final_Fibonacci)
        i += 1    
    return lista_fibonacci

def altera_salarios(salarios):
    ''' Calcule o aumento de salário de acordo com a seguinte tabela:
    - até 1 SM(inclusive): aumento de 20%
    - de 1 até 2 SM(inclusive): aumento de 15%
    - de 2 até 5 SM(inclusive): aumento de 10%
    - acima de 5 SM: aumento de 5% 
    Salário mínimo para referência: R$ 724,00
    Retorna a lista com os salários alterados
    '''
    salario_minimo = 724.00
    lista_aumento_salario = []
    i = 0
    while i < len(salarios):
        #até 1
        if salarios[i] <= salario_minimo:
            novo_salario = salarios[i] + ((salarios[i]) * (20/100))
        #1 a 2
        elif salarios[i] > salario_minimo and salarios[i] <= (salario_minimo * 2):
            novo_salario = salarios[i] + ((salarios[i]) * (15/100))
        #2 a 5
        if salarios[i] > (salario_minimo * 2) and salarios[i] <= (salario_minimo * 5):
            novo_salario = salarios[i] + ((salarios[i]) * (10/100))
        #mais que 5
        if salarios[i] > (salario_minimo * 5):
            novo_salario = salarios[i] + ((salarios[i]) * (5/100))
            
        lista_aumento_salario.append(novo_salario)
        i += 1
    return lista_aumento_salario

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
    print ('%s Esperado: %s \tObtido: %s' % (prefixo,repr(esperado), 
        repr(obtido)))

def main():
    print(' Meses acima da média:')
    test(media_anual([20,20,20,20,20,20,20,20,20,20,20,20]), [])
    test(media_anual([25,20,20,20,20,20,20,20,20,20,20,20]), [0])
    test(media_anual([23,25,26,24,21,22,26,24,25,22,23,19]), [1,2,3,6,7,8])
    test(media_anual([19,20,21,20,17,18,19,20,22,21,20]), [1, 2, 3, 7, 8, 9, 10])
    test(media_anual([21,22,23,21,22,22,23,21,23,22,21,23,21]), [1,2,4,5,6,8,9,11])
    
    print(' Alturas abaixo da media:')
    test(maiores_13([13,13,14],[1.7,1.7,1.5]), [1.5])
    test(maiores_13([13,13,14,13],[1.7,1.7,1.5,1.6]), [1.5])
    test(maiores_13([14,20],[1.6,2]), [1.6])
    test(maiores_13([10,7,13,15,20,21],[1.7,1.21,1.65,2,1.9,1.5]), [1.5])
    test(maiores_13([14,15,16,17,18,30],[1.9,1.89,1.85,1.95,2,1.99]), [1.9,1.89,1.85])
    test(maiores_13([10,9,90,9,13,14,15],[1.25,1.3,1.7,1.41,1.5,1.55,1.7]), [])

    print(' Média dos saltos em lista:')
    test(media_saltos_lista([10,10,10,10,10]), 10)
    test(media_saltos_lista([9,9.1,8,7,6.9]), 8)
    test(media_saltos_lista([1,1,3,5,5]), 3)
    test(media_saltos_lista([10,10,9.9,10,10]), 10)

    print(' Lista de primos:')
    test(lista_de_primos(0,1), [])
    test(lista_de_primos(5,10), [5,7])
    test(lista_de_primos(10,20), [11,13,17,19])
    test(lista_de_primos(0,21), [2,3,5,7,11,13,17,19])
    test(lista_de_primos(43,102), [43,47,53,59,61,67,71,73,79,83,89,97,101])

    print(' Fibonacci:')
    test(Fibonacci(1), [1])
    test(Fibonacci(2), [1,1])
    test(Fibonacci(3), [1,1,2])
    test(Fibonacci(4), [1,1,2,3])

    print(' Aumenta salários:')
    test(altera_salarios([500,724.0,725.00,1448.00,1449.00,3620.00,3621.00,4000.00]), 
        [600.0, 868.8, 833.75, 1665.2, 1593.9, 3982.0, 3802.05, 4200.0])

if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" %(total, acertos,
     total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
