#uso de aspas
mensagem = "Ele disse: 'Olá!'"
print(mensagem)

nomes = ["Alice", "Bob", "Carlos"]
    # Bloco de código a ser executado para cada elemento
    # do laço
for nome in nomes:
    print(nome)

# Exemplo de loop com while
contador = 0

while contador < 5:
    print(contador)
    contador += 1

# Saída:
# 0
# 1
# 2
# 3
# 4

# Exemplo de variáveis
nome = "João"
idade = 30
cidade = "São Paulo"

# Criando a mensagem com várias variáveis usando f-strings
mensagem = f"Olá, meu nome é {nome}, tenho {idade} anos e moro em {cidade}."
print(mensagem)



nome = "Alice"  # Definindo uma string
tamanho_nome = len(nome)  # Obtendo o tamanho da string usando len()
print(tamanho_nome)  # Exibindo o tamanho da string

numeros = [1, 2, 3, 4, 5]  # Definindo uma lista
tamanho_numeros = len(numeros)  # Obtendo o tamanho da lista usando len()
print(tamanho_numeros)  # Exibindo o tamanho da lista

tupla = (10, 20, 30)  # Definindo uma tupla
tamanho_tupla = len(tupla)  # Obtendo o tamanho da tupla usando len()
print(tamanho_tupla)  # Exibindo o tamanho da tupla

frutas = ["maçã", "banana", "laranja"]  # Definindo uma lista de frutas

if "banana" in frutas:  # Verificando se "banana" está presente na lista
    print("A fruta banana está presente na lista de frutas.")  # Exibindo uma mensagem se "banana" está presente

# Definindo uma string
texto = "Olá, mundo!"

# Extraindo os primeiros 4 caracteres
primeiros_caracteres = texto[:4]  # Resultado: "Olá,"

# Extraindo os caracteres a partir do índice 5 até o final
restante = texto[5:]  # Resultado: "mundo!"

# Extraindo um intervalo específico
intervalo = texto[2:6]  # Resultado: "á, m"

# Extraindo caracteres alternados
alternados = texto[::2]  # Resultado: "Oámno"

# Extraindo a string ao contrário
reverso = texto[::-1]  # Resultado: "!odnum ,álO"

# Definindo uma string em minúsculas
texto = "olá, mundo!"

# Convertendo para maiúsculas
texto_maiusculo = texto.upper()

print(texto_maiusculo)  # Saída: "OLÁ, MUNDO!"

# Definindo uma string em maiúsculas
texto = "OLÁ, MUNDO!"

# Convertendo para minúsculas
texto_minusculo = texto.lower()

print(texto_minusculo)  # Saída: "olá, mundo!"

# Definindo uma string com espaços em branco
texto = "   Olá, mundo!   "

# Removendo espaços em branco
texto_sem_espacos = texto.strip()

print(texto_sem_espacos)  # Saída: "Olá, mundo!"

# Definindo variáveis
nome = "Alice"
idade = 25

# Formatando uma string com valores
mensagem = "Olá, meu nome é {} e tenho {} anos.".format(nome, idade)

print(mensagem)  # Saída: "Olá, meu nome é Alice e tenho 25 anos."

# Definindo variáveis
nome = "Bob"
idade = 30

# Formatando uma string com índices e formatação avançada
mensagem = "Meu nome é {1} e tenho {0:0>2d} anos.".format(idade, nome)

print(mensagem)  # Saída: "Meu nome é Bob e tenho 30 anos."

#string methods

# Definindo uma string
texto = "Olá, mundo! Como você está?"

# Dividindo a string em uma lista de substrings
substrings = texto.split()

print(substrings)  # Saída: ['Olá,', 'mundo!', 'Como', 'você', 'está?']

# Definindo uma lista de números como strings
numeros = ["1", "2", "3", "4", "5"]

# Concatenando os elementos da lista em uma string com hífen como separador
texto = "-".join(numeros)

print(texto)  # Saída: "1-2-3-4-5"

# Definindo uma string
texto = "O rato roeu a roupa do rei de Roma."

# Substituindo uma substring na string
novo_texto = texto.replace("roeu", "comeu")

print(novo_texto)  # Saída: "O rato comeu a roupa do rei de Roma."

# Definindo uma string
texto = "Python é uma linguagem de programação."

# Verificando se a string começa com uma determinada substring
resultado = texto.startswith("Python")

print(resultado)  # Saída: True

# Definindo uma string
texto = "12345"

# Verificando se a string contém apenas dígitos(númericos)
resultado = texto.isdigit()

print(resultado)  # Saída: True

# Definindo uma string
texto = "Hello, world!"

# Verificando se a string contém apenas letras
resultado = texto.isalpha()

print(resultado)  # Saída: False

# Definindo uma string
texto = "Python é uma linguagem de programação poderosa."

# Encontrando a posição da substring
posicao = texto.find("linguagem")

print(posicao)  # Saída: 14

# Definindo uma string
texto = "Python é uma linguagem de programação poderosa."

# Contando o número de ocorrências da substring
ocorrencias = texto.count("a")

print(ocorrencias)  # Saída: 6