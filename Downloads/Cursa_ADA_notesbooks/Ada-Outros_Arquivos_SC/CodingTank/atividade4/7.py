"""Faça um programa que, dadas duas listas de mesmo tamanho, crie uma nova lista com cada elemento igual a soma dos elementos da lista 1 com os da lista 2, na mesma posição."""

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

new_list = []

for i in range(len(list1)):
    sum = list1[i] + list2[i]
    new_list.append(sum)

print(" Nova lista:", new_list)
