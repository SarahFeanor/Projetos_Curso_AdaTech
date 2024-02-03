"""Faça um programa que mostre o fatorial de um número digitado.
Exemplo
número digitado: 5
resultado esperado: 120
"""

numero = int(input("Digite um número: "))
resultado = 1

for i in range(1, numero + 1):
    resultado *= i

print("O fatorial de", numero, "é:", resultado)
