#!/bin/env python3
# coding: utf-8
# Marilia Ribeiro da Silva <marilia.ifc@gmail.com>
# Lista de exercícios 4

# Exercícios sem for, apenas com while e sem funções embutidas.

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
    

def dar_troco(valor_a_pagar, valor_em_dinheiro):
    ''' Calcule o troco numa lista com notas de 1,2,5,10,20,50 com sua 
    quantidade de notas sem considerar centavos
    ex: 1 e 10 retorna troco_notas_quantidade = [5,2] quantidade_notas = [1,2] 
    valor a pagar = 1
    valor pago  = 10
    troco = 9
    notas_troco = 5 e 2
    qtd_notas = 1 de 5R$ e 2 de 2R$'''
    notas = [50,20,10,5,2,1]
    i = 0
    valor_troco = valor_em_dinheiro - valor_a_pagar
    troco_notas_quantidade = []
    
    while valor_troco > 0:
        if valor_troco >= notas[i]:
            troco_notas_quantidade.append((notas[i], int(valor_troco / notas[i])))
            valor_troco = valor_troco % notas[i]
        else:
            i += 1
    return troco_notas_quantidade

def im_pares(lista):
    ''' Separe em listas os impares e pares, dos inteiros da 'lista' '''
    i = 0
    impares = []
    pares = []
    while i < len(lista):
        if lista[i] % 2 == 0:
            pares.append(lista[i])
        else:
            impares.append(lista[i])
        i += 1
    return (pares, impares)

def ondernamento_contrario(lista):
    ''' Inverta a lista '''
    i = len(lista)
    invertida = []
    while i > 0:
        invertida.append(lista[i-1])
        i -= 1
    return invertida

def intercalamento_listas(lista1,lista2):
    ''' Usando 'lista1' e 'lista2', ambas do mesmo comprimento,
    crie uma nova lista composta pelo
    intercalamento entre as duas.'''
    i= 0
    lista3=[]
    while  i < len(lista2):
        lista3.append(lista1[i])
        lista3.append(lista2[i])
        #lista3.append((lista1[i],lista2[i]))
        i += 1
    return lista3
    

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
    lista1 = [1,2,3,4,5,6,7,8,9,10]
    lista2 = [-1,0]
    lista3 = [-10,0,10,2,100,-100,-100.1]
    lista4 = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
    lista5 = [1,3,5,7,9]
    lista6 = [2,4,6,8,10]

    print(' Maior e o menor da lista:')
    test(maior_menor(lista1), (10,1))
    test(maior_menor(lista2), (0,-1))
    test(maior_menor(lista3), (100,-100.1))
    test(maior_menor(lista4), (-1,-10))

    print(' Troco do pagamento:')
    test(dar_troco(10,109), [(50,1),(20,2),(5,1),(2,2)])
    test(dar_troco(10,10), [])
    test(dar_troco(10,1), [])
    test(dar_troco(10,148), [(50,2),(20,1),(10,1),(5,1),(2,1),(1,1)])

    print(' Lista de pares e impares:')
    test(im_pares(lista1), ([2,4,6,8,10],[1,3,5,7,9]))
    test(im_pares(lista5), ([],[1,3,5,7,9]))
    test(im_pares(lista6), ([2,4,6,8,10],[]))

    print(' Listas invertidas:')
    test(ondernamento_contrario(lista1), ([10,9,8,7,6,5,4,3,2,1]))
    test(ondernamento_contrario(lista2), ([0,-1]))
    test(ondernamento_contrario(lista3), ([-100.1,-100,100,2,10,0,-10]))

    print(' Lista Intercalada:')
    test(intercalamento_listas(lista5,lista6), [1,2,3,4,5,6,7,8,9,10])

if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" %(total, acertos,
     total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
