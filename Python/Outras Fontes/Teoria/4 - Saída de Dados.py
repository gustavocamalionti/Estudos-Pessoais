n1 = bool(input('digite algo(testando bool): '))
print(n1)

print('2 é igual a 3?', 2 == 3)
print('2 é diferente de 3?', 2 != 3)

n = input('Digite algo (testando isnumeric - númerico?):')
print(n.isnumeric()) #isnumeric diz se é possível converter o valor em um número ou um tipo primitivo antes dele

n = input('Digite algo (testando isalpha - alfabético?):')
print(n.isalpha())

n = input('Digite algo (testando isalnum - alfabético numerico?):')
print(n.isalnum())

n = input('Digite algo (testando isupper - letras maiúsculas?):')
print(n.isupper())