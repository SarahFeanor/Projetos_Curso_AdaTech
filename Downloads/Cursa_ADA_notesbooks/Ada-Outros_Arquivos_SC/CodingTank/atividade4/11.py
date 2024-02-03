"""Faça um Programa que peça as 4 notas bimestrais e mostre a média, usando listas.
"""

grades = []
for i in range(4):
    grade = float(input("Insira sua nota do {}ª bimestre: ".format(i + 1)))
    grades.append(grade)
total = sum(grades)
average = total / len(grades)

print("A média é :", (average))
