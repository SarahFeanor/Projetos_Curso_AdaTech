"""Faça um programa que pede para o usuário digitar 5 números e, ao final, imprime uma lista com os 5 números digitados pelo usuário (sem converter os números para int ou float).
"""

numbers = []
for i in range(5):
    num = input("Digite um numero: ")
    numbers.append(num)
print("Listas de números: ")
for num in numbers:
    print(num)

