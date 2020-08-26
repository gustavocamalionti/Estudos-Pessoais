frase = 'Curso em Vídeo Python'
frase2 = '   Curso em Vídeo Python  '

#FATIAMENTO
f = 'FATIAMENTO'
print(f'{f:-^90}')
print(frase) #escrever o objeto.
print(frase[3]) #apenas o caracter n°.
print(frase[3:12]) #do caracter n°3 até o n°12.
print(frase[:13]) #inicio não definido até o n°13.
print(frase[13:]) #do caracter n°13 até um final não definido.
print(frase[0:15]) #do caracter n°0 até o n°15.
print(frase[:15]) #inicio não definido até o n°15.
print(frase[::2]) #inicio e final não definido pulando de 2 em 2.

#ANÁLISE
a = 'ANÁLISE'
print(f'{a:-^90}')
len(frase) #contador de caracteres, começando do 0.
len(frase2) #espaços contam caracteres. 
print(len(frase)) #mostrar na tela o valor contado. 
print(frase.count('o')) #contagem de quantos 'o' o objeto 'frase' possui.
print(frase.find('deo')) #posição do caracter que começa a palavra 'deo'. 
print(frase.find('Android')) #string não existe, não há nenhum android no objeto. 
print('Curso' in frase) #Curso está na frase? True. 

#TRANSFORMAÇÃO
n = 'TRANSFORMAÇÃO'
print(f'{n:-^90}')
print(frase.replace('Python', 'Android')) #Substitui Python por Android
print(frase.upper()) #Mantém os caracteres que estão em M e transforma o resto em m.
print(frase.lower()) #Mantém os caracteres que estão em m e transforma o resto em M.
print(frase.capitalize()) #Primeiro algarismo em Maiúsculo e o resto em minúsculo. 
print(frase.title()) #Todas as palavras começam com letra maiúsculas. 
print(frase.strip()) #Remove espaços desnecessarios da direita e esquerda. 
print(frase.rstrip()) #remove espaços desnecessários da direita. 
print(frase.lstrip()) #remove espaços desnecessários da esquerda. 

#DIVISÃO
d = 'DIVISÃO'
dividido = frase.split()
print(f'{d:-^90}')
print(frase.split()) #Divide cada palavra em um novo agrupamento de caracteres.
print(dividido) #novo objeto com o objeto 'frase' dividida, split aplicada.
print(dividido[0]) #novos agrupamentos, mostrar o '0'. 
print(dividido[2]) #novos agrupamentos, mostrar o '2'.
print(dividido[2][3]) #novos agrupamentos, mostrar o '2' com o '3' caracter.

#JUNÇÃO
j = 'JUNÇÃO'
print(f'{j:-^90}')
print('-'.join(frase)) #Junta todos os agrupamentos dividindo as palavras com '-'.

#COMBINANDO FUNÇÕES A OBJETOS
c = 'COMBINANDO FUNÇÕES A OBJETOS'
print(f'{c:-^90}')
print(frase.upper().count('O')) #Conta 'O', com a frase transformada(Maiúsc).
print(frase.lower().find('vídeo')) #Conta 'vídeo', com a frase transformada(Minúsc).

