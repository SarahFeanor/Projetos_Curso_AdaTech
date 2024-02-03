"""User
Agora usando o método max() faça um programa que imprima os três maiores números de uma lista."""


list_num = [10, 5, 25, 7, 15, 30, 1, 20]


biggest1 = max(list_num)
print(biggest1)
list_num.remove(biggest1)


biggest2 = max(list_num)
print(biggest2)
list_num.remove(biggest2)


biggest3 = max(list_num)
print(biggest3)

print("Os três maioress números são:", biggest1, biggest2, biggest3)