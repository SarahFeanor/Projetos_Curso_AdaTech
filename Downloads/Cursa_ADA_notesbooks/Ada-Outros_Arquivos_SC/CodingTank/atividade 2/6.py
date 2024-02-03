#Faça um programa que mostre uma questão de múltipla escolha com 5 opções (letras a, b, c, d, e).
# Sabendo a resposta certa, o programa deve receber a
# opção do usuário e informar a letra que o usuário marcou e se a resposta está certa ou errada.


print("Qual é a capital do Brasil?")
print("a) Brasília ")
print("b) São Paulo")
print("c) Rio de Janeiro")
print("d) Salvador")
print("e) Belo Horizonte")

resposta_usuario = input("Digite a letra da opção escolhida: ")

if resposta_usuario == "a" or resposta_usuario == "A":
    print("Você marcou a opção:", resposta_usuario)
    print("Resposta correta!")
else:
    print("Você marcou a opção:", resposta_usuario)
    print("Resposta incorreta!")
