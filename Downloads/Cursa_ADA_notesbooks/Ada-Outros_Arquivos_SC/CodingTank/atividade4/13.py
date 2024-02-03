"""Faça um programa que sorteia 10 números entre 0 e 100 e conte quantos números sorteados são maiores que 50.
"""

numbers = [12, 34, 67, 89, 23, 56, 78, 90, 45, 80]
count = 0

for number in numbers:
    if number > 50:
        count += 1

print("Maiores que 50: ", count)
