# Criando uma lista
lista = [1, 2, 3, 4, 5]

# Adicionando elementos à lista
lista.append(6)  # Adiciona o valor 6 ao final da lista
print(lista)  # Saída: [1, 2, 3, 4, 5, 6]

# Removendo um elemento da lista
lista.remove(3)  # Remove o valor 3 da lista
print(lista)  # Saída: [1, 2, 4, 5, 6]

# Acessando um elemento da lista pelo seu índice
elemento = lista[2]  # Acessa o elemento de índice 2 (valor 4)
print(elemento)  # Saída: 4

# Verificando o comprimento da lista
comprimento = len(lista)
print(comprimento)  # Saída: 5

# Verificando se um valor está presente na lista
presente = 4 in lista
print(presente)  # Saída: True

# Ordenando a lista em ordem crescente
lista.sort()
print(lista)  # Saída: [1, 2, 4, 5, 6]

# Revertendo a ordem dos elementos na lista
lista.reverse()
print(lista)  # Saída: [6, 5, 4, 2, 1]

# Copiando uma lista
copia = lista.copy()
print(copia)  # Saída: [6, 5, 4, 2, 1]

# Limpando todos os elementos da lista
lista.clear()
print(lista)  # Saída: []

# Criando uma lista
lista = ['a', 'b', 'c', 'd', 'e']

# Acessando elementos da lista pelo índice
primeiro_elemento = lista[0]  # Acessa o primeiro elemento ('a')
segundo_elemento = lista[1]  # Acessa o segundo elemento ('b')
terceiro_elemento = lista[2]  # Acessa o terceiro elemento ('c')

print(primeiro_elemento)  # Saída: 'a'
print(segundo_elemento)  # Saída: 'b'
print(terceiro_elemento)  # Saída: 'c'

# Criando uma lista
lista = [1, 2, 3, 4, 5]

# Percorrendo a lista com um loop for
for elemento in lista:
    print(elemento)
    
# Saída:
# 1
# 2
# 3
# 4
# 5

# Criando uma lista
lista = [1, 2, 3, 4, 5]

# Definindo uma função para dobrar o valor de um elemento
def dobrar(numero):
    return numero * 2

# Aplicando a função a cada elemento da lista usando map()
lista_dobrada = list(map(dobrar, lista))
print(lista_dobrada)  # Saída: [2, 4, 6, 8, 10]
# Criando uma lista
lista = [1, 2, 3, 4, 5]

# Usando a compreensão de lista para dobrar cada elemento
lista_dobrada = [elemento * 2 for elemento in lista]
print(lista_dobrada)  # Saída: [2, 4, 6, 8, 10]

# Exemplo de loop while para percorrer uma lista
lista = [1, 2, 3, 4, 5]
indice = 0

while indice < len(lista):
    elemento = lista[indice]
    print(elemento)
    indice += 1

# Saída:
# 1
# 2
# 3
# 4
# 5

# Exemplo de loop for para percorrer uma lista
lista = [1, 2, 3, 4, 5]

for elemento in lista:
    print(elemento)

# Saída:
# 1
# 2
# 3
# 4
# 5

# Criando uma lista
lista = [1, 2, 3, 4, 5]

# Removendo e retornando o último elemento da lista
ultimo_elemento = lista.pop()
print(ultimo_elemento)  # Saída: 5
print(lista)  # Saída: [1, 2, 3, 4]

# Removendo e retornando um elemento específico da lista pelo índice
elemento_removido = lista.pop(2)  # Remove e retorna o elemento de índice 2
print(elemento_removido)  # Saída: 3
print(lista)  # Saída: [1, 2, 4]