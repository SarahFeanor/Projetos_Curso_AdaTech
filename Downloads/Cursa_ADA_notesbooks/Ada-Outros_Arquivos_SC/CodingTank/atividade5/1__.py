# Escreva uma função que calcule e retorne o dobro de um número inserido. Teste este caso solicitando ao usuário que insira um número e após isso, retorne a resposta.

def calcular_dobro(numero):
    return numero * 2

numero = float(input("Digite um número: "))
print(f"O dobro de {numero} é: {calcular_dobro(numero)}")
