"""
Faça uma função que emita uma saudação baseada no horário. A função deve receber o nome e o horário (apenas número inteiro) e emita a mensagem com as seguintes condições:
até meio dia (não incluso): "Bom dia, (VARIAVEL_NOME)"
entre meio dia (incluso) e 18h (não incluso): "Boa tarde, (VARIAVEL_NOME)"
após as 18h (incluso): "Boa noite, (VARIAVEL_NOME)"""

def saudacao(nome, horario):
    if horario < 12:
        mensagem = "Bom dia"
    elif horario >= 12 and horario < 18:
        mensagem = "Boa tarde"
    else:
        mensagem = "Boa noite"

    return f"{mensagem}, {nome}"

nome = input("Digite seu nome: ")
horario = int(input("Digite o horário (apenas número inteiro): "))

print(saudacao(nome, horario))
