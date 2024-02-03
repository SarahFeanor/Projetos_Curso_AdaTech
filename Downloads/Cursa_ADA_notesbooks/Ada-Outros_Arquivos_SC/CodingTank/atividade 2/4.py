"""
Faça um programa que leia a validade das informações:
a. Idade: entre 0 e 150;

b. Salário: maior que 0;

c. Sexo: M, F ou Outro;

O programa deve imprimir uma mensagem de erro para cada informação inválida.
"""

idade = int(input("Digite sua idade: "))

if idade < 0 or idade > 150:
    print("Erro: digite uma idade válida entre 0 e 150, por favor.")

salario = float(input("Digite seu salário: "))
if salario <= 0:
    print("Erro: digite um salário válido maior que 0 .")

sexo = input("Digite seu sexo (M, F ou Outro): ")
if sexo != "M" and sexo != "F" and sexo != "Outro":
    print("Erro: digite um sexo válido, digite M, F ou Outro.")


idade = int(input("Digite sua idade: "))

while idade < 0 or idade > 150:
    print("Erro: digite uma idade válida entre 0 e 150, por favor.")
    idade = int(input("Digite sua idade: "))

salario = float(input("Digite seu salário: "))

while salario <= 0:
    print("Erro: digite um salário válido maior que 0.")
    salario = float(input("Digite seu salário: "))

sexo = input("Digite seu sexo (M, F ou Outro): ")

while sexo != "M" and sexo != "F" and sexo != "Outro":
    print("Erro: digite um sexo válido, digite M, F ou Outro.")
    sexo = input("Digite seu sexo (M, F ou Outro): ")

print("Idade:",idade,"\n""Salário:",salario,"\n""Sexo:",sexo,)
