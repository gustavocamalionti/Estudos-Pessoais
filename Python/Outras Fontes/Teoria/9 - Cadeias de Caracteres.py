frase = 'Curso em Vídeo Python'
frase2 = '   Curso em Vídeo Python  '

#FATIAMENTO
print('FATIAMENTO')
print(frase) #escrever o objeto.
print(frase[3]) #apenas o caracter n°.
print(frase[3:12]) #do caracter n°3 até o n°12.
print(frase[:13]) #inicio não definido até o n°13.
print(frase[13:]) #do caracter n°13 até um final não definido.
print(frase[0:15]) #do caracter n°0 até o n°15.
print(frase[:15]) #inicio não definido até o n°15.
print(frase[::2]) #inicio e final não definido pulando de 2 em 2.

#Análise
len(frase) #contador de algarismos começando do 0.
len(frase2) #espaços contam caracteres. 
print(len(frase)) #mostrar na tela o valor contado. 
print(frase.count('o')) #contagem de quantos 'o' o objeto 'frase' possui.
print(frase.find('deo')) #posição do caracter que começa a palavra 'deo'. 
print(frase.find('Android')) #string não existe, não há nenhum android no objeto. 
print('Curso' in frase) #Curso está na frase? True. 



#Combinando funções a objetos
print('combinando funções a objetos')
print(frase.upper().count('O')) #conta quantos caracteres são "O", tendo em vista que a frase foi transformada inteira em maiuscula pela função 'upper'.

