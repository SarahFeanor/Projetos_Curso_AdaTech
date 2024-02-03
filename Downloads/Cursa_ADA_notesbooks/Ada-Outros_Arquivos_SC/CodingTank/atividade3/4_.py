"""Faça um programa em que o usuário digite números quaisquer que encerrará no momento em que o valor 0 seja digitado. Ao final diga qual foi o maior número digitado."""

maior_numero = 0
numero = int(input("Digite um número (digite 0 para encerrar): "))

while numero != 0:
    if numero > maior_numero:
        maior_numero = numero
    numero = int(input("Digite um número (digite 0 para encerrar): "))

print("O maior número digitado foi:", maior_numero)
