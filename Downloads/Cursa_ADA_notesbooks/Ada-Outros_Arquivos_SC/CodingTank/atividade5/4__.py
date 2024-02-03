"""Faça uma função que verifique se um número é par. Teste esta função solicitando ao usuário que digite um número e emitindo a mensagem adequada caso o número seja par ou não.
 """
def verificar_par(numero):
    return numero % 2 == 0

numero = int(input("Digite um número: "))

if verificar_par(numero):
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
