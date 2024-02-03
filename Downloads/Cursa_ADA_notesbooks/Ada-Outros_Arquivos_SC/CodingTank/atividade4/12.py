""" #Crie uma lista com 10 números quaisquer:


list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a. uma lista com os 4 primeiros números

first_four = list_number[:4]

# b. uma lista com os 5 últimos números
last_five = list_number[5:]

# c. uma lista contendo apenas os elementos das posições pares
even_positions = list_number[1::2]

# d. uma lista contendo apenas os elementos das posições ímpares
odd_positions = list_number[0::2]

# e. a lista inversa da lista sorteada (isto é, uma lista que começa com o último elemento da lista sorteada e termina com o primeiro)
reversed_list = list_number[::-1]

# f. uma lista inversa dos 5 primeiros números
reversed_first_five = list_number[4::-1]

# g. uma lista inversa dos 5 últimos números.
reversed_last_five= list_number[:5][::-1]

"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# a.  Uma lista com os primeiros 4 números
first_four = []
for i in range(4):
    first_four.append(numbers[i])

# b.  Uma lista com os últimos 5 números
last_five = []
for i in range(len(numbers) - 5, len(numbers)):
    last_five.append(numbers[i])

# c. Uma lista contendo apenas os elementos em posições pares
even_positions = []
for i in range(1, len(numbers), 2):
    even_positions.append(numbers[i])

# d. Uma lista contendo apenas os elementos em posições ímpares
odd_positions = []
for i in range(0, len(numbers), 2):
    odd_positions.append(numbers[i])

# e. A lista reversa da lista original
reversed_list = []
for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

# f.Uma lista reversa dos primeiros 5 números
reversed_first_five = []
for i in range(4, -1, -1):
    reversed_first_five.append(numbers[i])

# g.  Uma lista reversa dos últimos 5 números
reversed_last_five = []
for i in range(len(numbers) - 1, len(numbers) - 6, -1):
    reversed_last_five.append(numbers[i])

print("a. First four numbers:", first_four)
print("b. Last five numbers:", last_five)
print("c. Elements at even positions:", even_positions)
print("d. Elements at odd positions:", odd_positions)
print("e. Reversed list:", reversed_list)
print("f. Reversed first five numbers:", reversed_first_five)
print("g. Reversed last five numbers:", reversed_last_five)







