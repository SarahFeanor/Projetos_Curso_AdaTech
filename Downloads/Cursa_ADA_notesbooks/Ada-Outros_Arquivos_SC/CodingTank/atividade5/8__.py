"""Faça uma função que calcula o fatorial de um número."""

def calcular_fatorial(numero):
    if numero < 0:
        return None
    elif numero == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

numero = int(input("Digite um número: "))

print(f"O fatorial de {numero} é: {calcular_fatorial(numero)}")
