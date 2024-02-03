

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# O método especial __init__() é chamado quando uma nova instância da classe é criada.
# Ele é usado para inicializar os atributos da instância. Neste exemplo, definimos
# os atributos 'nome' e 'idade' da instância da classe Pessoa.


# Método __str__()

class Pessoa:
    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

# O método especial __str__() é chamado quando a função built-in str() é chamada
# em uma instância da classe. Ele deve retornar uma representação legível em
# string da instância. Neste exemplo, retornamos uma string contendo o nome e a
# idade da pessoa.


# Método __repr__()

class Pessoa:
    def __repr__(self):
        return f"Pessoa('{self.nome}', {self.idade})"

# O método especial __repr__() é chamado quando a função built-in repr() é chamada
# em uma instância da classe. Ele deve retornar uma representação em string que
# pode ser usada para reproduzir a instância. Neste exemplo, retornamos uma string
# que segue a sintaxe para criar uma nova instância da classe Pessoa com os mesmos
# valores de 'nome' e 'idade'.


# Método __eq__()

class Pessoa:
    def __eq__(self, other):
        return self.nome == other.nome and self.idade == other.idade

# O método especial __eq__() é chamado quando o operador de igualdade (==) é usado
# para comparar duas instâncias da classe. Ele deve retornar True se as instâncias
# forem consideradas iguais e False caso contrário. Neste exemplo, comparamos os
# atributos 'nome' e 'idade' das duas instâncias.


# Método __lt__()

class Pessoa:
    def __lt__(self, other):
        return self.idade < other.idade

# O método especial __lt__() é chamado quando o operador de menor que (<) é usado
# para comparar duas instâncias da classe. Ele deve retornar True se a instância
# atual for menor que a instância 'other' e False caso contrário. Neste exemplo,
# comparamos as idades das duas instâncias.


# Método __gt__()

class Pessoa:
    def __gt__(self, other):
        return self.idade > other.idade

# O método especial __gt__() é chamado quando o operador de maior que (>) é usado
# para comparar duas instâncias da classe. Ele deve retornar True se a instância
# atual for maior que a instância 'other' e False caso contrário. Neste exemplo,
# comparamos as idades das duas instâncias.


# Método __len__()

class Pessoa:
    def __len__(self):
        return len(self.nome)

# O método especial __len__() é chamado quando a função built-in len() é chamada
# em uma instância da classe. Ele deve retornar um valor inteiro representando o
# tamanho da instância. Neste exemplo, retornamos o tamanho do atributo 'nome' da
# instância.


# Método __getitem__()

class Pessoa:
    def __getitem__(self, index):
        return self.nome[index]

# O método especial __getitem__() é chamado quando um elemento da instância é
# acessado usando a sintaxe de indexação []. Ele permite tratar a instância como
# uma sequência e acessar seus elementos por índice. Neste exemplo, retornamos o
# caractere do atributo 'nome' da instância no índice especificado.


# Método __setitem__()

class Pessoa:
    def __setitem__(self, index, value):
        self.nome = self.nome[:index] + value + self.nome[index+1:]

# O método especial __setitem__() é chamado quando um elemento da instância é
# atribuído usando a sintaxe de indexação []. Ele permite modificar um elemento
# específico da instância. Neste exemplo, atualizamos o caractere do atributo
# 'nome' da instância no índice especificado com o novo valor.


# Método __delitem__()

class Pessoa:
    def __delitem__(self, index):
        self.nome = self.nome[:index] + self.nome[index+1:]

# O método especial __delitem__() é chamado quando um elemento da instância é
# excluído usando a palavra-chave 'del' e a sintaxe de indexação []. Ele permite
# remover um elemento específico da instância. Neste exemplo, removemos o caractere
# do atributo 'nome' da instância no índice especificado.


# Método __contains__()

class Pessoa:
    def __contains__(self, value):
        return value in self.nome

# O método especial __contains__() é chamado quando a palavra-chave 'in' é usada
# para verificar se um valor está presente na instância. Ele deve retornar True
# se o valor estiver presente e False caso contrário. Neste exemplo, verificamos
# se o valor está presente no atributo 'nome' da instância.


# Método __call__()

class Pessoa:
    def __call__(self):
        print("Chamando a instância de Pessoa")

# O método especial __call__() é chamado quando uma instância da classe é chamada
# como uma função. Ele permite que a instância se comporte como uma função. Neste
# exemplo, quando a instância é chamada, uma mensagem é impressa.


# Método __enter__() e __exit__()

class Pessoa:
    def __enter__(self):
        print("Entrando no contexto")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Saindo do contexto")

# Os métodos especiais __enter__() e __exit__() são chamados quando uma instância
# da classe é usada em uma cláusula 'with'. Eles permitem que a instância entre e
# saia de um contexto específico. Neste exemplo, uma mensagem é impressa quando a
# instância entra e sai do contexto.

# Exemplos de uso da classe e seus métodos

# Criando uma instância da classe Pessoa
pessoa1 = Pessoa("João", 25)

# Utilizando o método __str__()
print(pessoa1)
# Resultado: Nome: João, Idade: 25

# Utilizando o método __repr__()
print(repr(pessoa1))
# Resultado: Pessoa('João', 25)

# Criando outra instância da classe Pessoa
pessoa2 = Pessoa("Maria", 30)

# Utilizando o método __eq__()
print(pessoa1 == pessoa2)
# Resultado: False

# Utilizando o método __lt__()
print(pessoa1 < pessoa2)
# Resultado: True

# Utilizando o método __gt__()
print(pessoa1 > pessoa2)
# Resultado: False

# Utilizando o método __len__()
print(len(pessoa1))
# Resultado: 4

# Utilizando o método __getitem__()
print(pessoa1[1])
# Resultado: "o"

# Utilizando o método __setitem__()
pessoa1[0] = "J"
print(pessoa1.nome)
# Resultado: "João"

# Utilizando o método __delitem__()
del pessoa1[1]
print(pessoa1.nome)
# Resultado: "Jo"

# Utilizando o método __contains__()
print("J" in pessoa1)
# Resultado: True

# Utilizando o método __call__()
pessoa1()
# Resultado: "Chamando a instância de Pessoa"

# Utilizando o método __enter__() e __exit__()
with pessoa1:
    print("Executando no contexto")
# Resultado:
# Entrando no contexto
# Executando no contexto
# Saindo do contexto

# Método __init__()

