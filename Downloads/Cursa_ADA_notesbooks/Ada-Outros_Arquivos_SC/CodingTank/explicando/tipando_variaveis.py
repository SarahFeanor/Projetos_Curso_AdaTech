# Números inteiros
x = 42
print(type(x))  # Saída: <class 'int'>

# Números de ponto flutuante
y = 3.14
print(type(y))  # Saída: <class 'float'>

# Números complexos
z = 1 + 2j
print(type(z))  # Saída: <class 'complex'>


#tipar em função
def somar(a: int, b: int) -> int:
    return a + b


print(somar(14, 12))

#tipar numa variavel
x = float(1)