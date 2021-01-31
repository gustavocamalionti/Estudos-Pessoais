#1
def soma(a, b):
    print(f'a = {a} e b = {b}.')
    s = a + b
    print(f'A soma a + b = {s}.')

#Programa Principal

soma(2, -4)
soma(3, 6)
soma(a=5, b=2)
soma(a=2, b=25)

#2
def contador(*núm):
    tamanho = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tamanho} números.')

#PRINCIPAL
contador(5,7,9,2,3)
contador(2,8,6,0)
contador(1,8)

#3
def contador2(*núm):
    for valor in núm:
        print(f'{valor}', end='')
    print(' FIM!')

#PRINCIPAL
contador2(5,7,9,2,3)
contador2(2,8,6,0)
contador2(1,8)

#4
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] = lst[pos]*2
        pos = pos + 1

valores = [0,3,2,7]
dobra(valores)
print(valores)


#5
def soma(*valores):
    s = 0
    for num in valores:
        s = s + num
    print(f'Somando {valores} temos que a soma vale {s}')

soma(2,6)
soma(2,9)

