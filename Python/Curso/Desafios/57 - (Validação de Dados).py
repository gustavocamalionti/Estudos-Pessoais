#Desafio 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.


sexo = str(input('Informe seu sexo: [M/F]? ')).strip().upper()[0]
while sexo not in 'MF': #while sexo !='F' and sexo !='M':
    sexo = str(input('Dado inválido. Digite novamente: ')).strip().upper()
idade = int(input('Informe sua idade: '))
print(f'Seu sexo é [{sexo}] e tem [{idade}] anos. Registro completo.')
