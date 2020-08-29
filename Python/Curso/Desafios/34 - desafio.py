#Desafio 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# #Para salários superiores a R$1250.00, calcule um aumento de 10%. 
# #Para os inferiores ou iguais, o aumento é de 15% 

salario = float(input(' Você como funcionário recebe quanto? '))

if salario>1250:
    print(f'Parabéns! Você acaba de ganhar um aumento de 10% no salário. De {salario:.2f} irá para {(salario+(salario*0.10)):.2f}')
else:
    print(f'Parabéns! Você acaba de ganhar um aumento de 15% no salário. De {salario:.2f} irá para {(salario+(salario*0.15)):.2f}')