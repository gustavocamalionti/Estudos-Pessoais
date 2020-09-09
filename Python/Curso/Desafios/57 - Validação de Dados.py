#Desafio 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo2 = ''
while sexo2 !='M' or sexo2 !='F':
    sexo = str(input('Informe seu sexo: [M/F]? ')).strip().upper()
    sexo2 = str(input('Dados inválidos. Por favor, informe seu sexo: ))
print('Muito obrigado!')