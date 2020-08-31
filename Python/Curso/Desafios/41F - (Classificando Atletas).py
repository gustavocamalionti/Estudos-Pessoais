#Desafio 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#  - Até 9 anos: MIRIM
#  - Até 14 anos: INFANTIL
#  - Até 19 anos: JUNIOR
#  - Até 20 anos: SÊNIOR
#  - Acima: MASTER

idade = int(input('Qual a sua idade? '))

if idade<=9:
    print(f'Com {idade} anos, você se enquadrará na categoria MIRIM. ')
elif 9<idade<=14:
    print(f'Com {idade} anos, você se enquadrará na categoria INFANTIL. ')
elif 14<idade<=19:
    print(f'Com {idade} anos, você se enquadrará na categoria JUNIOR. ')
elif 19<idade<=20:
    print(f'Com {idade} anos, você se enquadrará na categoria SÊNIOR. ')
elif idade>20: 
    print(f'Com {idade} anos, você se enquadrará na categoria MASTER. ')