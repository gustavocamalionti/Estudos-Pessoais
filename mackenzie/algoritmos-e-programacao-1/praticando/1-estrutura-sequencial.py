# EXERCÍCIO 1 – Escreva um programa em Python que permita ao usuário digitar dois números inteiros e exibir o resultado para cada uma das seguintes operações: soma, subtração, multiplicação, divisão, divisão truncada, resto e exponenciação. 
n1 = int(input(''))
n2 = int(input(''))

print(f'{n1+n2}')
print(f'{n1-n2}')
print(f'{n1*n2}')
print(f'{n1/n2}')
print(f'{n1//n2}')
print(f'{n1%n2}')
print(f'{n1**n2}')
 
# EXERCÍCIO 2 – Faça um programa em Python que leia dois números inteiros e exiba o quadrado da diferença do primeiro valor pelo segundo. 
a = int(input(''))
b = int(input(''))

print(f'{(a-b)*(a-b):.1f}')

# EXERCÍCIO 3 – Faça um programa em Python que resolva o seguinte problema: 
# Um concurso possui um prêmio no montante de R$ 780.000,00 para dividir entre três ganhadores da seguinte forma: 
# - o primeiro ganhador receberá 46% do prêmio; 
# - o segundo ganhador receberá 32% do prêmio; 
# - o terceiro ganhador receberá o restante do prêmio. 
n1 = 780000

print(f'{n1*0.46:.1f}')
print(f'{n1*0.32:.1f}')
print(f'{n1*(1 - (0.46 + 0.32)):.1f}')

