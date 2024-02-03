while True:
    operacao = input("Digite a operação desejada (+, -, *, /) ou 'sair' para sair: ")

    if operacao.lower() == 'sair':
        print("Calculadora encerrada.")
        break

    if operacao not in ('+', '-', '*', '/'):
        print("Operação inválida. Tente novamente.")
        continue

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 == 0:
            print("Erro: Não é possível dividir por zero. Tente novamente.")
            continue
        resultado = num1 / num2

    print("Resultado:", resultado)

