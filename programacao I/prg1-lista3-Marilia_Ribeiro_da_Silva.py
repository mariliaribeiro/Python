#!/bin/env python3
# coding: utf-8
# Marila Ribeiro da Silva <marilia.ifc@gmail.com>
# Lista de exercícios 3

def crescimento_populacional(populacao1,populacao2,crescimento1,crescimento2):
    ''' Calcule quantos anos levará para a 'população1' ultrapassar a 
    'população2', baseado em suas porcentagens de crescimento.'''
    anos = 0
    while populacao1 <=  populacao2 and crescimento1 > crescimento2:
        populacao1 += populacao1 * (crescimento1/100)
        populacao2 += populacao2 * (crescimento2/100)
        anos += 1
    return anos

def quantidade_de_impares(valor_inicial,valor_final):
    ''' Determine a quantidade de números ímpares num intervalo'''
    impares = 0
    valor_final -= 1
    while valor_inicial < valor_final:
        if (valor_inicial % 2) != 0:
            impares += 1
        valor_inicial += 1
    return impares

def soma_dos_inteiros(valor1,valor2):
    ''' Calcule a soma dos números inteiros no intervalo entre 'valor1'
    e o 'valor2' ou vice-versa, considerando que podem ser informado
    números negativos ou fora de ordem. 
    Ex: 1 e 5 ou 5 e 1, retorna 9'''
    soma = 0
    if valor1< valor2:
        x = valor1 + 1
        while x < valor2:
            soma += x
            x +=1
        return soma
    else:
        x = valor2 + 1
        while x < valor1:
            soma += x
            x += 1
        return soma

def potencia(base,expoente):
    ''' Calcule a 'base' elevada ao 'expoente' manualmente sem usar 
    'base**expoente'. Considere base e expoente como inteiros positivos.''' 
    i = 0
    while i <= expoente:
        pot = pow(base,expoente)
        i += 1
    return pot

def Fibonacci(n):
    ''' Retorne o n-ésimo valor da série de Fibonacci
    Fibonacci = 1,1,2,3,5,8,13,...'''
    i = 0
    anterior = 1
    final_Fibonacci = 1
    while i < n:
        armazena = final_Fibonacci
        final_Fibonacci = final_Fibonacci + anterior
        anterior = armazena
        i += 1
    return final_Fibonacci

def fatorial(numero):
    ''' Calcule e retorne o fatorial do 'numero' informado,
    O fatorial é o valor produtório dos valores menores ou iguais ao número
    ex: fatorial de 4 é 4*3*2*1 e retorna 24'''
    i = 1
    valor_fatorial = 1
    if numero == 0:
        valor_fatorial = 0
    while i <= numero:
        valor_fatorial *= i
        i += 1
    return valor_fatorial

def primo(valor):
    ''' Verifique se o 'valor' informado é primo.
    Um número primo é aquele que é divisível apenas por ele mesmo e por 1
    1 não é primo.'''
    x = 0
    while x <= valor:
        if valor == 2 or valor == 3 or valor == 5 or valor == 7:
            return True
        if valor == 1 or valor % 2 == 0 or valor % 3 == 0 or valor % 5 == 0 or valor % 7 == 0:
            return False
        if (x % 2 != 0 or x % 3 != 0 or x % 5 != 0 or x % 7 != 0) and x % 1 == 0 and x % x == 0:
            return True
        x += 1

def quantidade_de_primos(comeco,final):
    ''' Retorne a quantidade de primos entre os valores informados.
    Dica: use a função primo() recém desenvolvida para fazer a verificação.'''
    qt_primos = 0
    while comeco < final:
        if primo(final) == True:
            qt_primos += 1
        final -= 1
    return qt_primos

def media_saltos(salto1,salto2,salto3,salto4,salto5):
    ''' Calcule a media dos saltos de um atleta, sabendo que o melhor
    e o pior saltos são desconsiderados. '''
    lista = [salto1,salto2,salto3,salto4,salto5]
    minimo = min(lista)
    maximo = max(lista)
    media = ((salto1 + salto2 + salto3 + salto4 + salto5) - (minimo + maximo))/3
    return media
def serie1(fim):
    '''Dado n, calcule o valor de
    s = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n '''
    n = 1
    s = 0
    while n <= fim:
        s += float(1/n)
        n +=1
    return round(s,2)

def serie2(fim):
    '''Dado n, calcule o valor de
    s = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m'''
    m = 1
    n = 1
    s = 0
    while n <= fim:
        s += float(n/m) 
        m +=2
        n+=1
    return round(s,2)

def serie_pi(numero_vezes):
    ''' Calcule o valor de pi através da série
    4/1 - 4/3 + 4/5 - 4/7 + ... - 4/n, sendo n informado '''
    n = 1
    pia = 0
    i = 0
    base = 4.0
    while i < numero_vezes:
        pia +=base/n
        base = - base
        i += 1
        n +=2
    return round(pia,6)

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
    print('Aumento da população:')
    test(crescimento_populacional(80000,200000,3,1.5), 63)
    test(crescimento_populacional(1000,2000,1,1.1), 0)
    test(crescimento_populacional(2000,1000,1.1,1), 0)
    test(crescimento_populacional(2000,2020,1.1,1), 11)

    print('Quantidade de ímpares:')
    test(quantidade_de_impares(1,50), 24)
    test(quantidade_de_impares(1,10), 4)
    test(quantidade_de_impares(1,60), 29)
    test(quantidade_de_impares(40,80), 19) #20

    test(soma_dos_inteiros(1,5), 9)
    test(soma_dos_inteiros(1,50), 1224)
    test(soma_dos_inteiros(50,1), 1224)
    test(soma_dos_inteiros(10,1), 44)
    test(soma_dos_inteiros(-10,1), -45)
    test(soma_dos_inteiros(10,-10), 0)

    print('Potência:')
    test(potencia(1,20000), 1)
    test(potencia(2,4), 16)
    test(potencia(10000,1), 10000)
    test(potencia(2,10), 1024)

    print('Fibonnaci:')
    test(Fibonacci(8), 55)
    test(Fibonacci(9), 89)
    test(Fibonacci(10), 144)
    test(Fibonacci(1), 2)

    print('Fatorial:')
    test(fatorial(5), 120)
    test(fatorial(10), 3628800)
    test(fatorial(0), 0)
    test(fatorial(1), 1)

    print('Primo:')
    test(primo(5), True)
    test(primo(10), False)
    test(primo(0), False)
    test(primo(43), True)
    
    print('Quantidade de primos no intervalo:')
    test(quantidade_de_primos(5,10), 1)
    test(quantidade_de_primos(10,20), 4)
    test(quantidade_de_primos(0,21), 8)
    test(quantidade_de_primos(43,102), 12)

    print('Média dos saltos:')
    test(media_saltos(10,10,10,10,10), 10)
    test(media_saltos(9,9.1,8,7,6.9), 8)
    test(media_saltos(1,1,3,5,5), 3)
    test(media_saltos(10,10,9.9,10,10), 10)

    print('Série 1:')
    test(serie1(1), 1.00)
    test(serie1(15), 3.32)
    test(serie1(10), 2.93)
    test(serie1(5), 2.28)

    print('Série 2:')
    test(serie2(1), 1.00)
    test(serie2(2), 1.67)
    test(serie2(3), 2.27)
    test(serie2(4), 2.84)

    print('Série pi:')
    test(serie_pi(1), 4.000000)
    test(serie_pi(2), 2.666667)
    test(serie_pi(3), 3.466667)
    test(serie_pi(4), 2.895238)
    test(serie_pi(5), 3.339683)
    test(serie_pi(6), 2.976046)
    test(serie_pi(7), 3.283738)
    test(serie_pi(8), 3.017072)
    test(serie_pi(9), 3.252366)
    test(serie_pi(10), 3.041840)
    test(serie_pi(100), 3.131593)
    test(serie_pi(150), 3.134926)
    test(serie_pi(1000), 3.140593)
    test(serie_pi(5000), 3.141393)
    test(serie_pi(9000), 3.141482)

if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" %(total, acertos,
     total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
