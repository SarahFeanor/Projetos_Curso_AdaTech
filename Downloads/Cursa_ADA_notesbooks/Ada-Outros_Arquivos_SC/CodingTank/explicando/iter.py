# Criando uma lista
lista = ['a', 'b', 'c', 'd']

# Obtendo um iterador a partir da lista usando a função iter()
iterador = iter(lista)

# Iterando sobre o iterador usando um loop while
while True:
    try:
        # Obtendo o próximo elemento do iterador usando a função next()
        elemento = next(iterador)
        print(elemento)
    except StopIteration:
        # A exceção StopIteration é lançada quando não há mais elementos no iterador
        break


# Definição da classe Car (carro)
class Car:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"{self.brand} está dirigindo nas ruas.")

# Definição da classe Boat (barco)
class Boat:
    def __init__(self, name):
        self.name = name

    def sail(self):
        print(f"{self.name} está navegando no oceano.")

# Definição da classe Plane (avião)
class Plane:
    def __init__(self, model):
        self.model = model

    def fly(self):
        print(f"{self.model} está voando nos céus.")

# Função que demonstra o polimorfismo
def travel(vehicle):
    vehicle.drive()  # Chamada do método "drive()" para todos os veículos
    vehicle.sail()   # Chamada do método "sail()" somente para barcos
    vehicle.fly()    # Chamada do método "fly()" somente para aviões

# Criação de objetos das classes Car, Boat e Plane
car = Car("Ferrari")
boat = Boat("Titanic")
plane = Plane("Boeing 747")

# Chamada da função "travel()" para diferentes objetos
print("Viagem de Carro:")
travel(car)   # O objeto "car" é tratado como um veículo

print("\nViagem de Barco:")
travel(boat)  # O objeto "boat" é tratado como um veículo

print("\nViagem de Avião:")
travel(plane)  # O objeto "plane" é tratado como um veículo
