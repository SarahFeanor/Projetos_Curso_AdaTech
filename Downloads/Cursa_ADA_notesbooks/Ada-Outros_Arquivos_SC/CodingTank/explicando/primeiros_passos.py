# python3 index.py run pelo terminal

# recomendado_uso_de_snake_case

mensagem = "Olá, mundo!"
print(mensagem)

# Solicitar ao usuário que insira seu nome
nome = input("Digite seu nome: ")

# Exibir uma mensagem com o nome fornecido pelo usuário
print("Olá,", nome, "!")

x = 10  # Variável global

def minha_funcao():
    print(x)  # Acessando a variável global dentro da função

print(x)  # Acessando a variável global fora da função
minha_funcao()

def minha_funcao():
    y = 5  # Variável local
    print(y)

minha_funcao()
print(y)  # Isso causará um erro, pois y é uma variável local e não está acessível fora da função