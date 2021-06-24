#Desafio 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

#A média de idade do grupo.
#Qual é o nome do homem mais velho.
#Quantas mulheres têm menos de 20 anos.
somaF = 0
somamédia = 0
maiorM = 0
menorF = 0
velho = ''
nova = ''

for c in range(1,5):
    titulo = (f'{c}° PESSOA')
    print(f'{titulo:-^30}')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somamédia = somamédia + idade
    
    if c==1 and sexo == 'M':
        maiorM = idade 
        velho = nome 
        
    if idade>maiorM and sexo == 'M':
        maiorM = idade
        velho = nome

    if idade<20 and sexo == 'F':
        menorF = idade
        nova = nome
        somaF = somaF + 1

print(f'A média de idade do grupo é de {somamédia/4} anos.') 
print(f'O homem mais velho tem {maiorM} anos e se chama {velho}.') 
print(f'Há {somaF} mulheres com menos de 20 anos e a mais nova se chama {nova}.')    

