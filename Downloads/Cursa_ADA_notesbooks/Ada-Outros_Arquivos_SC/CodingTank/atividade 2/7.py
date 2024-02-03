print("Responda as seguintes perguntas com 1 ou 0 :")

a = int(input("Mora perto da vítima? "))
b = int(input("Já trabalhou com a vítima? "))
c = int(input("Telefonou para a vítima? "))
d = int(input("Esteve no local do crime? "))
e = int(input("Devia para a vítima? "))

pontuacao = 0

if a == 1:
    pontuacao += a

if b == 1:
    pontuacao += b

if c == 1:
    pontuacao += c

if d == 1:
    pontuacao += d

if e == 1:
    pontuacao += e

print("Sua pontuação é ", pontuacao)

if pontuacao == 5:
  print('Assassino')
elif (pontuacao == 3) or (pontuacao == 4): # 3 <= pontuacao <= 4
  print('Cúmplice')
elif pontuacao == 2:
  print('Suspeito')
else:
  print('Liberado')