# Faça uma calculadora.
#  O usuário deve inserir qual a operação matemática ele deseja realizar e logo em seguida os dois números.
# O programa deve finalizar apenas quando o usuário digitar a opção "sair" no momento de escolha da operação matemática.


# Inicio do lado com determinação que haja  apenas resultados válidos em relação ao sair:
# O while True cria um loop infinito que só é interrompido quando a condição de saída é atendida.

while True:

    operacao = input(
        "Digite a operação desejada \n soma(+) \n subtração(-) \n multiplicação (*)\n divisão (/) \n ou digite (sair) para sair: ")
# Esse parte inclui que o sair pode ser em maiusculo, ao digitar sair a gente "breka" a operação e "printa" uma mensagem para o usuário.
    if operacao.lower() == "sair":
        print("Calculadora encerrada.")
        break
# tratamento de erro no caso de digitar a operacao errada
    if operacao not in ["+", "-", "*", "/"]:
        print("Operação inválida. Por favor, tente novamente.")
        continue
# o usuário é solicitado que digite os algorismos para a  operação ser realizada
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
# aqui são as operações realizadas
    if operacao == "+":
        resultado = num1 + num2
        print("O resultado da soma é:", resultado)
    elif operacao == "-":
        resultado = num1 - num2
        print("O resultado da subtração é::", resultado)
    elif operacao == "*":
        resultado = num1 * num2
        print("O resultado da multiplicação é::", resultado)
# tratamento de erro para prosseguir o programa
    elif operacao == "/":
        if num2 != 0:
            resultado = num1 / num2
            print("O resultado da divisão é::", resultado)
        else:
            print("Erro: divisão por zero não é possível. \n Por favor, tente novamente!")
    else:
        print("Operação inválida. Por favor, tente novamente.")
