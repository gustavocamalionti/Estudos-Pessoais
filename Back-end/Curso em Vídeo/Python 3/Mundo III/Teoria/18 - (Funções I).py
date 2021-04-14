#Exemplo sem função
a = 4
b = 5
s = a + b
print(s)

a = 3
b = 8
s = a + b
print(s)

print('-'*30)

#1)Exemplo com Função
def soma1(a, b):
    s = a + b
    print(s)


#1.1) Programa Principal 
soma1(4, 5)
soma1(3, 8)
soma1(4, 8)

print('-'*30)

#2)Exemplo com Função
def soma2(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de {a} e {b} é {s}')


#2.1) Programa Principal 
soma2(a = 4, b = 5)
soma2(b = 3,a = 8)
soma2(4, 8)

print('-'*30)

#3)Exemplo com Função
def contador(*núm):
    tam = len(núm)
    print(f'Recebi os valores {núm} e são {tam} números')


#3.1) Programa Principal 
contador(5,7,3,1,4)
contador(8,4,7)

print('-'*30)

#4)Exemplo com Função
def contador(*núm):
    tam = len(núm)
    print(f'Recebi os valores {núm} e são {tam} números')


#3.1) Programa Principal 
contador(5,7,3,1,4)
contador(8,4,7)