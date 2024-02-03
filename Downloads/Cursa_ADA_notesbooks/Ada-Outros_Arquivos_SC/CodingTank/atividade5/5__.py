"""Crie uma função que recebe duas listas. Caso estas duas listas sejam do mesmo tamanho some os elementos de cada lista com mesmo índica, caso contrário retorne uma lista vazia.
Se as duas listas de entrada forem do mesmo tamanho o programa deve se comportar como no exemplo:

lista_01 = [1, 2, 3, 4, 5]
lista_02 = [6, 7, 8, 9, 10]

soma_listas(lista_01, lista_02)
saída:

[7, 9, 11, 13, 15]"""


def soma_listas(lista1, lista2):
    if len(lista1) == len(lista2):
        soma = [lista1[i] + lista2[i] for i in range(len(lista1))]
        return soma
    else:
        return []

lista_01 = [1, 2, 3, 4, 5]
lista_02 = [6, 7, 8, 9, 10]

print(soma_listas(lista_01, lista_02))
