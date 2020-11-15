
num = [2,5,9,1]
num[2]=3 #Substituir a posição 2 pelo número 3.
print(f'Substituição: {num}')

num.append(7) #Aumentar +1 termo na lista na ultima posição
print(f'Aumento de termos: {num}')

num.sort() #Organizar em ordem crescente
print(f'Ordem Crescente{num}')

num.sort(reverse=True) #Organizar em ordem Decrescente
print(f'Ordem Decrescente{num}')

num.pop() #Exclui o último valor
print(f'último valor: {num}')

num.pop(3) #Remove um valor específico
print(f'valor específico: {num}')

num.insert(3, 2) #na posiçaõ destacada '3' insere um novo termo '2'
print(f'Insere na posição 3 o valor 2: {num}')

num.remove(5) #Remove um termo específico '5'
print(f'Remove o termo específico: {num}')

print(f'Essa lista tem {len(num)} Elementos') #Contador de elementos

#EXEMPLOS PRÁTICOS
if 5 in num:
    num.remove(5)
else:
    print('Nãao achei o 5')

valores = [] 
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v} ')
print('Cheguei ao final da lista!.')

valores2 = [] 

for cont in range(0,5):
    valores2.append(int(input('Digite um valor: ')))
print(valores2)

a = [2, 3, 4, 7]
b = a[:] #FATIAMENTO, B não é exatamente A, na verdade B está recebendo todos os valores de A. Portanto a[:] é um comando de cópia
b[2] = 8

print(f'{a}')
print(f'{b}')