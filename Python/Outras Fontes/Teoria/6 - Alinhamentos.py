nome = input('Qual é o seu nome? ')
print(f'Prazer em te conhecer, {nome:20}!') #Escrever algum nome em 20 caracteres.
print(f'Prazer em te conhecer, {nome:>20}!') #Escrever algum nome em 20 caracteres Alinhado a Direita.
print(f'Prazer em te conhecer, {nome:<20}!') #Escrever algum nome em 20 caracteres Alinhado a Esquerda.
print(f'Prazer em te conhecer, {nome:^20}!') #Escrever algum nome em 20 caracteres Alinhado ao centro.
print(f'Prazer em te conhecer, {nome:=^20}!') #Escrever algum nome no centro com 20 caracteres tendo iguais.
#print('prazer em te conhecer, {:=^20}'.format(nome))