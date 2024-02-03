#Escreva um programa que peça a nota de 3 provas de um aluno e verifique se ele passou ou não de ano. 
#Obs.: O aluno irá passar de ano se sua média for maior que 6.

nota1 = int(input("qual é a primeira nota do seu aluno?"))
nota2 = int(input("qual é a segunda nota do seu aluno?"))
nota3 = int(input("qual é a terceira nota do seu aluno?"))
media = (nota1 + nota2 + nota3)/3

if media >= 6:
    print('Seu aluno foi aprovado')
elif media < 6:
    print('Seu aluno não foi aprovado')