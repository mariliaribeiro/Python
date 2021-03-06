#!/bin/env python3
# coding: utf-8
# Marilia Ribeiro da Silva <marilia.ifc@gmail.com>
# Lista de exercícios 7a

def leet(texto):
    '''
    Converte texto em leet
    troca = {'a':'4','e':'3','g':'9','i':'1','s':'5','t':'7','o':'0'}
    '''
    troca_caracter_para_leet = dict([('a','4'),('e', '3'), ('g', '9'), ('i', '1'), ('s', '5'),('t', '7'),('o', '0')])
    
    novo_texto = ''
    for caracter in texto:
        if caracter.lower() in troca_caracter_para_leet:
            novo_texto += troca_caracter_para_leet[caracter.lower()]
        else:
            novo_texto += caracter
    return novo_texto

def conta_letras(texto):
    '''Receba uma string e devolva um dicionário onde a chave seja uma letra e seu 
    valor correspondente seja a quantidade de vezes que esta letra aparece na string, 
    independente de caixa (maiúscula ou minúscula)'''
    
    discionario_letras_quantidade = {}
    letra = list(texto)
    for letra in texto:
        if letra.lower() not in discionario_letras_quantidade:
            discionario_letras_quantidade[letra.lower()] = 1
        else:
            discionario_letras_quantidade[letra.lower()] += 1
    return discionario_letras_quantidade

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
    print ('leet')
    test(leet('ifc'), '1fc')
    test(leet('fisl2013'), 'f15l2013')
    test(leet('deco'), 'd3c0')
    test(leet('EMO'),'3M0')
    test(leet('restart'), 'r3574r7')
    test(leet('infeliz'), '1nf3l1z')
    test(leet('The Cure'), '7h3 Cur3')
    test(leet('Eu te amo'), '3u 73 4m0')

    print('conta letras')
    test(conta_letras("a"), {'a': 1})
    test(conta_letras("ana"), {'a': 2, 'n':1})
    test(conta_letras("bala"),  {'a': 2, 'b': 1, 'l': 1})
    test(conta_letras("bota"), {'a': 1, 'b': 1, 't': 1, 'o': 1})
    test(conta_letras("banana"), {'a': 3, 'b': 1, 'n': 2})
    test(conta_letras("abacaxi"), {'a': 3, 'x': 1, 'c': 1, 'b': 1, 'i': 1})
    test(conta_letras("araquari"), {'a': 3, 'q': 1, 'r': 2, 'u': 1, 'i': 1})
    test(conta_letras("Instituto Federal Catarinense"),  {'a': 3, ' ': 2, 'c': 1, 'e': 4, 'd': 1, 'f': 1, 'i': 3, 'l': 1, 'o': 1, 'n': 3, 's': 2, 'r': 2, 'u': 1, 't': 4})

if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" %(total, acertos,
     total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
