#!/bin/env python3
# coding: utf-8
# Marilia Ribeiro da Silva <marilia.ifc@gmail.com>
# Resolva os exercícios tentando usar compreensão de lista onde possível.
# Crie os testes para cada função

#Para estes exercícios, usaremos as listas abaixo:

mulheres = ['Mariana', 'Ana', 'Paula']
homens = ['Pedro', 'Juca', 'Tom', 'Joaquim']

#1. Use uma listcomp para gerar uma lista de homens com nomes de 4 ou menos letras.
def len_nomes(lista):
    return[lista[nome] for nome in range(len(lista)) if len(lista[nome]) <= 4]

#2. Use uma listcomp para gerar uma lista de duplas (também conhecida em 
#computação como uma lista associativa) formada pela letra inicial e o nome 
#de cada homem. Por exemplo, a resposta para a lista mulheres seria:
#[('M', 'Mariana'), ('A', 'Ana'), ('P', 'Paula')]
def tupla_nomes(lista):
    return [(nome[0], nome) for i, nome in enumerate(lista)]

#3. Use o resultado do exercício 2 para gerar um dicionário associando 
#iniciais aos nomes de homens. Quantos itens terá o dicionário assim produzido?

def dict_nomes(lista):
    return (len(dict([(nome[0], nome) for i, nome in enumerate(lista)])))

#4. Use a função zip para gerar uma lista associativa, e com ela carregar 
#um dicionário associando cada mulher a um homem. Quantos itens terá o 
#dicionário assim produzido?
def zip_dict(lista1,lista2):
    return len(dict([(m, n) for m, n in zip(lista1, lista2)]))
    
#5. Gere uma lista associativa para organizar uma aula de dança na qual 
#todos devem dançar com todos. Quantos casais serão formados?
#Dica: o nome da operação a ser feita neste exercício é produto cartesiano, 
#e para fazer isso em uma listcomp ou genexp você precisa usar mais de um 
#for dentro da expressão.
def produto_listas(lista1, lista2):
    return [(lista1[nome1], lista2[nome2]) for nome1 in range(len(lista1)) for nome2 in range(len(lista2))]

#6. Repita o exercício 5, acrescentando um filtro com if para remover os 
#nomes com menos de 4 letras das duas listas. Quantos casais serão formados?
def produto_listas_len_nomes(lista1, lista2):
    nomes_lista1, nomes_lista2 = len_nomes(lista1), len_nomes(lista2)
    return [(nomes_lista1[nome1], nomes_lista2[nome2]) for nome1 in range(len(nomes_lista1)) for nome2 in range(len(nomes_lista2)) if nomes_lista1 and nomes_lista2]
    

    
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
    print('Testes')
    print('\n Nomes menor que quatro digitos:')
    test(len_nomes(homens), ['Juca', 'Tom'])
    test(len_nomes(mulheres), ['Ana'])
    
    print('\n Nome e letra inicial:')
    test(tupla_nomes(homens), [('P','Pedro'), ('J','Juca'), ('T','Tom'), ('J','Joaquim')])
    test(tupla_nomes(mulheres), [('M','Mariana'), ('A','Ana'), ('P','Paula')])
    
    print('\n Quatidade de elementos de um dicionário:')
    test(dict_nomes(homens), 3)
    test(dict_nomes(mulheres), 3)
    
    print('\n Função zip:')
    test(zip_dict(homens, mulheres), 3)
    
    print('\n Produto cartesiano:')
    test(produto_listas(homens, mulheres), [('Pedro', 'Mariana'), ('Pedro', 'Ana'), ('Pedro', 'Paula'), ('Juca', 'Mariana'), ('Juca', 'Ana'), ('Juca', 'Paula'), ('Tom', 'Mariana'), ('Tom', 'Ana'), ('Tom', 'Paula'), ('Joaquim', 'Mariana'), ('Joaquim', 'Ana'), ('Joaquim', 'Paula')])
    
    print('\n Produto cartesiano com nomes menores que quatro dígitos:')
    test(produto_listas_len_nomes(homens, mulheres), [('Juca', 'Ana'), ('Tom', 'Ana')])
    
   

    #test(funcao(valores), valor_esperado)
    
        
if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" %(total, acertos,
     total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
