
soma = quant = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break 
    quant = quant + 1
    soma = soma + n
print(f'Obrigado, você forneceu {quant} números e a soma entre eles vale {soma}')