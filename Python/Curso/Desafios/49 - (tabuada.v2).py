#Desafio 049: Refaça o Desafio 009: mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um número: '))
print('A tabuada de {} vale: ')


for c in range(1, 11):
    print(f'{n} . {c} = {n*c}')