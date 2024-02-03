# Desafio: Sequência de Fibonacci
# Na matemática, a sequência de Fibonacci, é uma sequência de números inteiros, começando por 1 e 1, na qual cada termo subsequente corresponde à soma dos dois anteriores. Segue o exemplo:

# 1, 1, 2, 3, 5, 8, 13..

# Faça um programa (sem utilizar recursão) que dado um número irá imprimir na tela a sequência de Fibonacci até o índice dado, no exemplo acima o valor 13 possui índice 7, portanto ao passarmos 13 para a função ela deverá imprimir 8.
def fibonacci(indice):
    if indice <= 0:
        return None
    elif indice == 1:
        return 1
    elif indice == 2:
        return 1
    else:
        fib_seq = [1, 1]
        for i in range(2, indice):
            fib_num = fib_seq[i-1] + fib_seq[i-2]
            fib_seq.append(fib_num)
        return fib_seq[-1]

numero = int(input("Digite um número: "))

fibonacci_resultado = fibonacci(numero)
print(f"O número Fibonacci no índice {numero} é: {fibonacci_resultado}")
