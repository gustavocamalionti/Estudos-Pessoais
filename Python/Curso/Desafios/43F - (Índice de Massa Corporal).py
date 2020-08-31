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
    print('ABAIXO DO PESO.')
elif 18.5<=imc<25:
    print('com o PESO IDEAL.')
elif 25<=imc<30:
    print('com SOBREPESO.')
elif 30<=imc<40:
    print('com OBESIDADE.')
else:
    print('com OBESIDADE MÓRBIDA.')