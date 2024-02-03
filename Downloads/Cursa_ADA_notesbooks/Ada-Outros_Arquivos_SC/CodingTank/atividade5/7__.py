"""Faça uma função que recebe uma lista de números e calcula a média destes números."""

def calcular_media(lista):
    if len(lista) > 0:
        soma = sum(lista)
        media = soma / len(lista)
        return media
    else:
        return None

numeros = [2, 4, 6, 8, 10]
print(f"A média dos números é: {calcular_media(numeros)}")
