#Atividade 08 - LAB01

valor = float(input('Digite o valor da prestação: '))
taxa = float(input('Digite o valor em porcentagem da taxa: '))
tempo = int(input('Digite quantos meses tem de atraso: '))

print(f'O valor da prestação em atraso é: {(valor+(valor*(taxa/100)*tempo))}')

