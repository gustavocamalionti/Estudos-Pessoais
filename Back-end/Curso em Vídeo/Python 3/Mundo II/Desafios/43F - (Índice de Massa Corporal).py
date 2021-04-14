#Desafio 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#  - Abaixo de 18.5: Abaixo do Peso.
#  - Entre 18.5 e 25: Peso ideal.
#  - 25 até 30: Sobrepeso.
#  - 30 até 40: Obesidade.
#  - Acima de 40: Obesidade Mórbida.

peso = float(input('Digite o seu "peso": '))
altura = float(input('Qual a sua altura? '))
imc = peso/((altura)*2)

print(f'Com {peso:.2f}kg e tendo {altura:.2f}m, seu IMC é de {imc:.2f}. Portanto, você está ', end ='')
if imc<18.5:
    print('\033[37;41mABAIXO DO PESO\033[m.')
elif 18.5<=imc<25:
    print('com o \033[37;42mPESO IDEAL\033[m.')
elif 25<=imc<30:
    print('com \033[37;45mSOBREPESO\033[m.')
elif 30<=imc<40:
    print('com \033[37;47mOBESIDADE\033[m.')
else:
    print('com \033[37;41mOBESIDADE MÓRBIDA\033[m.')