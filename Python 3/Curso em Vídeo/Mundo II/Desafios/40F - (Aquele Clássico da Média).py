#Desafio 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#  - Média abaixo de 5.0? REPROVADO.
# - Média entre 5.0 e 6.9:RECUPERAÇÃO.
#  - Média 7.0 ou superior: APROVADO.

a = float(input('Nota na P1: '))
b = float(input('Nota na P2: '))

#VALIDAÇÃO DAS NOTAS
if a>10 or a<0 or b>10 or b<0:
    print(f'\033[37;41mNOTA INVALIDA!\033[m O sistema só aceitará valores entre 0 e 10. ')
    exit()

#CALCULO DAS MÉDIAS
media = (a+b)/2
if media < 5.0: 
    print(f'\033[37;41mREPROVADO!\033[m Sua média foi de \033[31m{media}\033[m. ')
if media >= 5 and media < 7: #7>media>=5
    print(f'\033[37;44mRECUPERAÇÃO!\033[m Sua média foi de \033[34m{media}\033[m.')
if media >= 7: #else: também funcionaria!
    print(f'\033[37;42mAPROVADO!\033[m Sua média foi de \033[32m{media}\033[m.')




a = float(input('Nota na P1: '))
b = float(input('Nota na P2: '))

#CALCULO DAS MÉDIAS
media = (a+b)/2
if 0 <= media < 5: 
    print(f'\033[37;41mREPROVADO!\033[m Sua média foi de \033[31m{media}\033[m. ')
elif media >= 5 and media < 7: #7>media>=5
    print(f'\033[37;44mRECUPERAÇÃO!\033[m Sua média foi de \033[34m{media}\033[m.')
elif 10 >= media >= 7: #else: também funcionaria!
    print(f'\033[37;42mAPROVADO!\033[m Sua média foi de \033[32m{media}\033[m.')
else:
    print(f'Média = \033[31m{media:.2f}\033[m. Essa média não existe, confira os valores de P1 e P2.')
