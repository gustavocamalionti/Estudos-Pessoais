#Desafio 077: Crie um programa que tenha uma tupla com várias palavras. (Não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Aprender', 'Ensinar', 'Cozinhar', 'Beber', 'Dançar', 'Curso', 'Gratis')


for p in palavras:
    print(f'\nNa palavra {p.upper()} temos como sílabas: ', end ='')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra.upper(), end=' ')
            
