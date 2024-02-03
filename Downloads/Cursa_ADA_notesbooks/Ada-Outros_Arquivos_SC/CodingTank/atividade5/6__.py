"""Utilize a mesma lógica do exercício anterior, porém agora você deve multiplicar os elementos ao invés de somá-los."""
def multiplicar_listas(lista1, lista2):
    if len(lista1) == len(lista2):
        multiplicacao = [lista1[i] * lista2[i] for i in range(len(lista1))]
        return multiplicacao
    else:
        return []

lista_01 = [1, 2, 3, 4, 5]
lista_02 = [6, 7, 8, 9, 10]

print(multiplicar_listas(lista_01, lista_02))
