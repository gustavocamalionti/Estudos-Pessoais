#Desafio 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: 
# a) Quantas vezes apareceu o valor 9. 
# b) Em que posição foi digitado o primeiro valor 3. 
# c) Quais foram os números pares. 


n1 = int(input('Digite o 1° valor: '))
n2 = int(input('Digite o 2° valor: '))
n3 = int(input('Digite o 3° valor: '))
n4 = int(input('Digite o 4° valor: '))


núm = (n1, n2, n3, n4)
print(f'Você digitou os valores {núm}')

print(f'Vezes que o 9 apareceu: {núm.count(9)}.')
if 3 in núm:
    print(f'A primeira vez que o 3 apareceu foi na {núm.index(3)+1}º posição. ')
else:
    print(f'O valor 3 não foi digitado nenhuma vez.')
print(f'Números Pares:', end = ' ')
for n in núm:
    if n%2==0:
        print(n, end=' ')
