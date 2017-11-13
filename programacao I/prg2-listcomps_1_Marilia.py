#!/bin/env python3
# coding: utf-8
# Marilia Ribeiro da Silva <marilia.ifc@gmail.com>
# Resolva os exercícios tentando usar compreensão de lista onde possível.

def pares_e_divisiveis_por_7(limite_inicial=1067, limite_final=3627):
    '''Entre 1067 e 3627 (inclusive), quantos números são pares e 
    também divisíveis por 7? 
    '''
    return len([x for x in range(limite_inicial, limite_final) if x % 2 == 0 and x % 7 == 0])

def duplica_caracter(s):
    '''
    Retorna os caracteres da string original duplicados
    duplica_caracter('The') -> 'TThhee'
    duplica_caracter('AAbb') -> 'AAAAbbbb'
    duplica_caracter('Hi-There') -> 'HHii--TThheerree'
    '''
    return ''.join([(s[i]*2) for i in range(len(s))])

def conta_pares(nums):
    '''
    Retorna a quantidade de números pares da lista
    conta_pares([2, 1, 2, 3, 4]) -> 3
    conta_pares([2, 2, 0]) -> 3
    conta_pares([1, 3, 5]) -> 0
    '''    
    return len([numero for numero in nums if numero % 2 == 0])

def gago(texto):
    '''Receba um texto e devolva-o repetindo a primeira letra de cada palavra, junto com um traço
    gago("preciso tirar dez") -> "p-preciso t-tirar d-dez"
    gago("eu deveria ter estudado mais") -> "e-eu d-deveria t-ter e-estudado m-mais"
    '''
    return ' '.join(['%s-%s' %(palavra[0], palavra) for i, palavra in enumerate(texto.split())])

def explode_string(s):
    '''
    explode_string('Code') -> 'CCoCodCode'
    explode_string('abc') -> 'aababc'
    explode_string('ab') -> 'aab'
    '''
    return ''.join([s[:letra+1] for letra in range(len(s))])
    
def intercalamento_listas(lista1,lista2):
    ''' Usando 'lista1' e 'lista2', ambas do mesmo comprimento,
    crie uma nova lista composta pelo
    intercalamento entre as duas.'''
    return sorted([numero for numero in (lista1 + lista2)])

def numeros_sortudos(limite_inferior=1, limite_superior=100000):
    ''' Daniela é uma pessoa muito supersticiosa. Para ela, um número é 
    sortudo se ele contém o dígito 2 mas não o dígito 7. 
    Faça então uma função que informe a ela quantos números sortudos 
    existem entre um intervalo dado, incluindo os extremos.
    Por exemplo: entre 18644 e 33087, existem 7995 números sortudos.
    Dica: faça uma função de validação e outra que a chama e 
    verifica o intervalo dado
    '''
    return len([numero for numero in range(limite_inferior, limite_superior) if '2' in str(numero) and '7' not in str(numero)])
    
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
    print('Pares e divisíveis por 7:')
    test(pares_e_divisiveis_por_7(), 183) 

    print ('duplica_caracter')
    test(duplica_caracter('The'), 'TThhee')
    test(duplica_caracter('AAbb'), 'AAAAbbbb')
    test(duplica_caracter('Hi-There'), 'HHii--TThheerree')
    test(duplica_caracter('Word!'), 'WWoorrdd!!')
    test(duplica_caracter('!!'), '!!!!')
    test(duplica_caracter(''), '')
    test(duplica_caracter('a'), 'aa')
    test(duplica_caracter('.'), '..')
    test(duplica_caracter('aa'), 'aaaa')  

    print ('conta_pares')
    test(conta_pares([2, 1, 2, 3, 4]), 3)
    test(conta_pares([2, 2, 0]), 3) # espera 3 - 2
    test(conta_pares([1, 3, 5]), 0) # 0 - 2
    test(conta_pares([]), 0)
    test(conta_pares([11, 9, 0, 1]), 1) # 1 -2
    test(conta_pares([2, 11, 9, 0]), 2)
    test(conta_pares([2]), 1)
    test(conta_pares([2, 5, 12]), 2)

    print('Gago')
    test(gago('O'), 'O-O')
    test(gago('O O'), 'O-O O-O')
    test(gago('Oi'), 'O-Oi')
    test(gago('beleza?'), 'b-beleza?')
    test(gago('tudo bem?'), 't-tudo b-bem?')
    test(gago('nota dez!'), 'n-nota d-dez!')
    test(gago('preciso tirar dez'), 'p-preciso t-tirar d-dez')
    test(gago('eu deveria ter estudado mais'), 'e-eu d-deveria t-ter e-estudado m-mais')
    
    print ('Explode string')
    test(explode_string('abc'), 'aababc')
    test(explode_string('ab'), 'aab')
    test(explode_string('x'), 'x')
    test(explode_string('aqui'), 'aaqaquaqui')
    test(explode_string('decai'), 'ddedecdecadecai')
    test(explode_string('Beleza'), 'BBeBelBeleBelezBeleza')
    test(explode_string('gago'), 'ggagaggago')    

    print(' Lista Intercalada:')
    test(intercalamento_listas([1,3,5,7,9],[2,4,6,8,10]), [1,2,3,4,5,6,7,8,9,10])

    print(' Números sortudos:')
    test(numeros_sortudos(18644,33087), 7995)
        
if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" %(total, acertos,
     total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
