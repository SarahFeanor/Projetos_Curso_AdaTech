"""
Faça um programa que mostre o fatorial de um número digitado.
Exemplo
número digitado: 5
resultado esperado: 120"""

numero_digitado = int(input("Digite um número inteiro: "))
resultado = 1
contador = 1

while contador <= numero_digitado:
    resultado *= contador
    contador += 1

print("O fatorial de", numero_digitado, "é:", resultado)
