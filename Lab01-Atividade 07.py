#Atividade 07 - LAB01

print('Informar o valor médio ponderado entre as quatro notas abaixo.')

nota1 = float(input("Nota 1:"))
peso1 = 1

nota2 = float(input("Nota 2:"))
peso2 = 2

nota3 = float(input("Nota 3:"))
peso3 = 3

nota4 = float(input("Nota 4:"))
peso4 = 4

media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3 + nota4 * peso4) / (peso1 + peso2 + peso3 + peso4)

print("Média das Notas:", media)