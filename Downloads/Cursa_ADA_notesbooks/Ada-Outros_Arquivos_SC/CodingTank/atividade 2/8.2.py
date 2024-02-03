
preco_antigo = float(input("Digite o valor do produto (preço antigo): "))
if preco_antigo <= 50:
    aumento = preco_antigo * 0.05
elif preco_antigo <= 100:
    aumento = preco_antigo * 0.1
elif preco_antigo <= 150:
    aumento = preco_antigo * 0.13
else:
    aumento = preco_antigo * 0.15

preco_novo = preco_antigo + aumento

if preco_novo <= 80:
    mensagem = "Barato"
elif preco_novo <= 115:
    mensagem = "Razoável"
elif preco_novo <= 150:
    mensagem = "Normal"
elif preco_novo <= 170:
    mensagem = "Caro"
else:
    mensagem = "Muito Caro"
print("Preço Novo: R$", preco_novo)
print("Mensagem:", mensagem)
