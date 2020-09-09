
#for c in range(1,11):
   # print(c)
#print('FIM')

#LIMITE DEFINIDO
c = 1
while c <= 10:
    print(c)
    c= c + 1 
print('FIM')

#LIMITE INDEFINIDO: 01
n = 1
while n!=0:
    n = int(input('Digite um valor: '))
print('FIM')

#LIMITE INDEFINIDO: 02
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper().strip()
print('FIM')

n = 1 
par = impar = 0
while n!=0:
    n = int(input('Digite um valor: '))
    if n!=0:
        if n%2==0:
            par = par + 1
        else:
            impar = impar + 1
print(f'você digitou {par} números pares e {impar} números impares.')