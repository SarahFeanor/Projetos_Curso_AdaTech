# Criando um dicionário
dicionario = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}

# Método keys()
print("Método keys():")
chaves = dicionario.keys()
print(chaves)

# Método values()
print("Método values():")
valores = dicionario.values()
print(valores)

# Método items()
print("Método items():")
itens = dicionario.items()
print(itens)

# Método get()
print("Método get():")
valor1 = dicionario.get('chave1')
valor4 = dicionario.get('chave4', 'Valor padrão')
print(valor1)
print(valor4)

# Método pop()
print("Método pop():")
valor_removido = dicionario.pop('chave2')
print(valor_removido)
print(dicionario)

# Método update()
print("Método update():")
outro_dicionario = {'chave4': 'valor4', 'chave5': 'valor5'}
dicionario.update(outro_dicionario)
print(dicionario)

# Método clear()
print("Método clear():")
dicionario.clear()
print(dicionario)

# Método copy()
print("Método copy():")
dicionario = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}
copia = dicionario.copy()
print(copia)

# Método setdefault()
print("Método setdefault():")
valor_padrao = dicionario.setdefault('chave4', 'Valor padrão')
print(valor_padrao)
print(dicionario)

# Método popitem()
print("Método popitem():")
par_chave_valor = dicionario.popitem()
print(par_chave_valor)
print(dicionario)
