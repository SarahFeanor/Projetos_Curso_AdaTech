# Crie uma função para cálculo do comprimento da circunferência (C = 2 * 3.14 * R), sendo C o comprimento e R o raio da circunferência

def calc_circunferencia(raio):
    return 2 * 3.14 * raio
raio = float(input("Digite o raio da circunferência: "))
print(f"O comprimento da circunferência é: {calc_circunferencia(raio)}")
