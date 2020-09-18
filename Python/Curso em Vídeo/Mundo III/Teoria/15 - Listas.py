
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

num.insert(2, 11) #na posiçaõ destacada '2' insere um novo termo '11'
print(f'Insere na posição 2 o valor 11: {num}')


print(f'Essa lista tem {len(num)} Elementos') #Contador de elementos
