#Desafio 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

#RESOLUÇÃO PESSOAL
c = 0
while True:
    n = int(input('Digite um número e te darei a tabuada dele: '))
    if n<0:
        break 
    while c<=10:
        c = c + 1
        print(f'{n} x {c} = {n*c}')
        if c == 10:
            c = 0
            break
print('Obrigado!')

#RESOLUÇÃO DO PROFESSOR:
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n<0:
        break
    for c in range(1,11):
        print(f'{c} x {n} = {c*n}')
print('Obrigado')