#Desafio 061: Refaça o desafio 051, lendo o primeiro termo e a razão de uma pa, mostrando os 10 primeiros termos da progressão usando a estrutura while.

#RESOLUÇÃO PESSOAL 
p = int(input('Digite o primeiro termo da PA: '))
rz = int(input('Qual a razão? '))
result = p

print(result, end = ' ')
while result != p+rz*9:
    result = result + rz 
    print(result, end=' ')
print('\n','-'*30)
print(f'\nO primeiro termo da PA é {p} \nA razão é de {rz} \nO 10° termo da PA vale {p+rz*9}')
