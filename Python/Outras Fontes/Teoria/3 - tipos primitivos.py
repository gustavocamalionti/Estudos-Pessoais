print('Sem especificar o tipo primitivo:str ')
n1 = input('Digite aqui um número inteiro: ')
print(type(n1))
print('apesar de {} ser da classe "numérica;int", o computador não entende isso e ele irá interpretar por padrão stringer. Assim, é necessário dizer para ele em qual tipo primitivo a sua variável se enquadrará.'.format(n1))

print('Especificando o tipo primitivo:int ')
n2 = int(input('Digite aqui um número Inteiro: '))
print(type(n2))
print('Agora especificando, o computador reconhece {} como "int".'.format(n2))

print('Especificando o tipo primitivo:float')
n3 = float(input('Digite aqui um valor real:'))
print(type(n3))

print('Especificando o tipo primitivo:str')
n4 = str(input('Digite aqui um caracter:'))
print(type(n4))

print('Especificando o tipo primitivo:bool')
n5 = bool(input('digita qualquer coisa:'))
print(type(n5))