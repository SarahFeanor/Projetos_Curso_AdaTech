"""Faça um programa que sorteia 10 números entre 0 e 100 e conte quantos números sorteados são maiores que 50.
"""
import random

numeros_sorteados = []
soma = 0

for _ in range(10):
    numero = random.randint(0, 100)
    numeros_sorteados.append(numero)
    soma += numero

maior_numero = max(numeros_sorteados)
menor_numero = min(numeros_sorteados)
media = soma / len(numeros_sorteados)

print("Números sorteados:", numeros_sorteados)
print("Maior número sorteado:", maior_numero)
print("Menor número sorteado:", menor_numero)
print("Média dos números sorteados:", media)
print("Soma dos números sorteados:", soma)
