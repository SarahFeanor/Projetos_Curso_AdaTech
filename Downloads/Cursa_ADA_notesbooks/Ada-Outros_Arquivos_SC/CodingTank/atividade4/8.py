"""Faça um programa que dadas duas listas de mesmo tamanho, imprima o produto escalar entre elas.
"""

list1 = [1, 2, 3]
list2 = [4, 5, 6]

product = dot_product(list1, list2)
if product is not None:
    print("Resultado", product)
else:
    print("Error: As lista devem ter o mesmo tamanho!!")
