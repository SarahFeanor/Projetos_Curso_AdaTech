"""Faça um script que peça para o usuário digitar a idade, o salário e o sexo de uma pessoa até que as entradas digitadas sejam válidas.
a. Idade: entre 0 e 150
b. Salário: maior que 0
c. Gênero: M, F ou Outro

Por último imprima os dados recebidos do usuário."""

while True:
    idade = int(input("Digite a idade: "))
    if 0 <= idade <= 150:
        break

while True:
    salario = float(input("Digite o salário: "))
    if salario > 0:
        break

while True:
    genero = input("Digite o gênero (M, F ou Outro): ")
    if genero in ['M', 'F', 'Outro']:
        break

print("Dados recebidos:")
print("Idade:", idade)
print("Salário: R$", salario)
print("Gênero:", genero)
