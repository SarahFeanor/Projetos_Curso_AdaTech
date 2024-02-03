# Função com parâmetros posicionais e parâmetros opcionais
def saudacao(nome, saudacao="Olá"):
    mensagem = f"{saudacao}, {nome}!"
    return mensagem

# Exemplo de uso da função
print(saudacao("João"))  # Saída: "Olá, João!"
print(saudacao("Maria", "Oi"))  # Saída: "Oi, Maria!"

# Função com número variável de argumentos posicionais e argumentos nomeados
def calcular_media(*numeros, **kwargs):
    soma = sum(numeros)  # Calcula a soma dos números fornecidos
    total = len(numeros)  # Calcula o total de números fornecidos
    media = soma / total  # Calcula a média
    if kwargs.get('arredondar', False):
        return round(media, kwargs.get('casas_decimais', 2))  # Arredonda a média com base nos argumentos nomeados
    return media

# Exemplo de uso da função
print(calcular_media(5, 8, 10))  # Saída: 7.666666666666667 (média sem arredondamento)
print(calcular_media(5, 8, 10, arredondar=True))  # Saída: 7.67 (média arredondada para 2 casas decimais)
print(calcular_media(5, 8, 10, casas_decimais=1))  # Saída: 7.7 (média arredondada para 1 casa decimal)

# Função com retorno múltiplo usando tupla
def calcular_estatisticas(numeros):
    soma = sum(numeros)
    media = soma / len(numeros)
    maior = max(numeros)
    menor = min(numeros)
    return soma, media, maior, menor

# Exemplo de uso da função
resultados = calcular_estatisticas([5, 8, 10, 3, 6])
print(resultados)  # Saída: (32, 6.4, 10, 3)
soma, media, maior, menor = resultados
print(f"Soma: {soma}, Média: {media}, Maior: {maior}, Menor: {menor}")
# Saída: Soma: 32, Média: 6.4, Maior: 10, Menor: 3

# Função com chamada recursiva para calcular o fatorial
def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

# Exemplo de uso da função
resultado = calcular_fatorial(5)
print(resultado)  # Saída: 120 (5! = 5 * 4 * 3 * 2 * 1 = 120)


# Exemplo de uso da função lambda

# Definição de uma função lambda que retorna o dobro de um número
dobro = lambda x: x * 2

# Utilizando a função lambda
resultado = dobro(5)
print(resultado)

# Resultado: 10

""" As funções lambda são úteis quando você precisa de uma função simples que pode ser definida em linha, sem a necessidade de criar uma função separada usando a palavra-chave def. Elas são frequentemente usadas em combinação com funções como map(), filter() e reduce(), que esperam receber funções como argumentos. """