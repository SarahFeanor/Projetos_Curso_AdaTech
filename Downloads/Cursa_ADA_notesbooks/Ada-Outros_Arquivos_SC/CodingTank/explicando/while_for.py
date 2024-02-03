# Exemplo do 'while' com 'break'

# Contador
contador = 0

# Loop while
while True:
    contador += 1

    # Verifica se o contador atingiu o valor 5
    if contador == 5:
        break  # Sai do loop quando o contador for igual a 5

    print(contador)

# Resultado:
# 1
# 2
# 3
# 4

# Exemplo do 'while' com 'continue'

# Contador
contador = 0

# Loop while
while contador < 5:
    contador += 1

    # Verifica se o contador é par
    if contador % 2 == 0:
        continue  # Pula para a próxima iteração do loop se o contador for par

    print(contador)

# Resultado:
# 1
# 3
# 5

# Exemplo do 'for' com listas aninhadas

# Lista de listas
alunos = [["João", 15], ["Maria", 16], ["Carlos", 14], ["Ana", 17]]

for _ in [16]:

  print("Python é demais!")

# Loop for para percorrer a lista de listas
for aluno in alunos:
    nome = aluno[0]
    idade = aluno[1]
    print(f"Aluno: {nome}, Idade: {idade}")

# Resultado:
# Aluno: João, Idade: 15
# Aluno: Maria, Idade: 16
# Aluno: Carlos, Idade: 14
# Aluno: Ana, Idade: 17

# Exemplo do 'for' com dicionário

# Dicionário de informações dos alunos
alunos = {
    "João": 15,
    "Maria": 16,
    "Carlos": 14,
    "Ana": 17
}

# Loop for para percorrer as chaves e valores do dicionário
for nome, idade in alunos.items():
    print(f"Aluno: {nome}, Idade: {idade}")

# Resultado:
# Aluno: João, Idade: 15
# Aluno: Maria, Idade: 16
# Aluno: Carlos, Idade: 14
# Aluno: Ana, Idade: 17

# Exemplo do 'for' usando a função 'range'

# Loop for para percorrer um intervalo de números
for i in range(1, 6):
    print(i)

# Resultado:
# 1
# 2
# 3
# 4
# 5
