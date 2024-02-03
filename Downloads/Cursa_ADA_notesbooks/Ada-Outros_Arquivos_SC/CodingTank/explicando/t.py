lista = [55, 16, 37, 23, 68, 97, 69, 85, 10, 15]
l1 = []
l2 = []

for x in lista:
  if x % 2 != 0:
    l1.append(lista[x])
  else:
    l2.append(lista[x])
    
print(l1)
print(l2)
