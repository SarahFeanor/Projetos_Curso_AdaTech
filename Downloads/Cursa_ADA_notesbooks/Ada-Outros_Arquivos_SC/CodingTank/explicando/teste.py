lista_inicial = lista = [55, 16, 37, 23, 68, 97, 69, 85, 10, 15]
l1 = []
l2 = []

for item in lista_inicial:
    if item % 2 == 0:
        if item < 0:
            lista_final.append(-item)  
        else:
            lista_final.append(item) 
    else:
        if item < 0:
            lista_final.append(-2*item) 
        else:
            lista_final.append(2*item) 

print(lista_final == [10, 10, 14, 6, 42, 126, 8, 10, 26])

animais = ['gato', 'coelho', 'macaco', 'girafa']

animais.remove('gato')
print(animais)
print(len(animais))
print(animais.index('coelho'))