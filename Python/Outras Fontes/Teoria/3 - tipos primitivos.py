print('Sem especificar o tipo primitivo ')
n1 = input('Digite aqui um número inteiro: ')
print(type(n1))
print('apesar de {} ser da classe "numérica;int", o computador não entende isso e ele irá interpretar por padrão stringer. Assim, é necessário dizer para ele em qual tipo primitivo a sua variável se enquadrará.'.format(n1))

print('Especificando o tipo primitivo ')
n2 = int(input('Digite aqui um número: '))
print(type(n1))
print('Agora especificando, o computador reconhece {} como "int".'.format(n2))