def obter_mensagem(preco):
    if preco <= 80:
        return "Barato"
    elif preco <= 115:
        return "Razoável"
    elif preco <= 150:
        return "Normal"
    elif preco <= 170:
        return "Caro"
    else:
        return "Muito Caro"

def calcular_aumento(preco_antigo):
    if preco_antigo <= 50:
        aumento = preco_antigo * 0.05
    elif preco_antigo <= 100:
        aumento = preco_antigo * 0.1
    elif preco_antigo <= 150:
        aumento = preco_antigo * 0.13
    else:
        aumento = preco_antigo * 0.15

    preco_novo = preco_antigo + aumento
    mensagem = obter_mensagem(preco_novo)
    return preco_novo, mensagem


preco_antigo = float(input("Digite o valor do produto (preço antigo): "))
preco_novo, mensagem = calcular_aumento(preco_antigo)
print("Preço Novo: R$", preco_novo)
print("Mensagem:", mensagem)