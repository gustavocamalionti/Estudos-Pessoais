#Desafio 024: Faça um programa que leia uma frase pelo teclado e mostre: 
# Quantas vezes aparece a letra "a". 
# Em que posição ela aparece a primeira vez. 
# Em que posição ela aparece a última vez.




#MODO 1:FEITO SOZINHO
frase = str(input('Escreva uma frase: ')).lower()

print('Analisando...')
print(f'A letra "a" apareceu {frase.count("a")} vezes na sua frase. ')
print(f'A primeira vez que ela apareceu foi na posição {frase.find("a")+1}') 
print(f'E a última vez foi na posição {frase.rfind("a")+1}. ')  #.rfind("a") começa a contar do lado direito.
