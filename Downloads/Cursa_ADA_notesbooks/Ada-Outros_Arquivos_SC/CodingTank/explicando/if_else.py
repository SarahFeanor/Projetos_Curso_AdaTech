# Exemplo de estrutura condicional if...else

# Variável de exemplo
idade = 18

# Verifica se a idade é maior ou igual a 18
if idade >= 18:
    # Bloco de código executado se a condição for verdadeira
    print("Você é maior de idade.")
else:
    # Bloco de código executado se a condição for falsa
    print("Você é menor de idade.")

# Resultado: "Você é maior de idade."

# Exemplo de estrutura condicional if...elif...else

# Variável de exemplo
nota = 85

# Verifica a nota e atribui uma classificação
if nota >= 90:
    # Bloco de código executado se a nota for maior ou igual a 90
    print("Classificação: A")
elif nota >= 80:
    # Bloco de código executado se a nota for maior ou igual a 80
    print("Classificação: B")
elif nota >= 70:
    # Bloco de código executado se a nota for maior ou igual a 70
    print("Classificação: C")
elif nota >= 60:
    # Bloco de código executado se a nota for maior ou igual a 60
    print("Classificação: D")
else:
    # Bloco de código executado se nenhuma das condições anteriores for verdadeira
    print("Classificação: F")

# Resultado: "Classificação: B"

# Exemplo do operador 'and'

# Variáveis de exemplo
idade = 25
possui_habilitacao = True

# Verifica se a pessoa pode dirigir
if idade >= 18 and possui_habilitacao:
    print("Você pode dirigir.")
else:
    print("Você não pode dirigir.")

# Resultado: "Você pode dirigir."

# Exemplo do operador 'or'

# Variáveis de exemplo
tem_passagem_comprada = False
tem_reserva_de_hotel = True

# Verifica se a pessoa pode viajar
if tem_passagem_comprada or tem_reserva_de_hotel:
    print("Você pode viajar.")
else:
    print("Você não pode viajar.")

# Resultado: "Você pode viajar."

# Exemplo do operador 'not'

# Variável de exemplo
chovendo = True

# Verifica se a pessoa precisa levar um guarda-chuva
if not chovendo:
    print("Não é necessário levar um guarda-chuva.")
else:
    print("É necessário levar um guarda-chuva.")

# Resultado: "É necessário levar um guarda-chuva."


