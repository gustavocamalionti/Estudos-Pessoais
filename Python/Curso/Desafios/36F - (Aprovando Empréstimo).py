#Desafio 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# - Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

vcasa = float(input('Quanto vale a casa que você quer comprar? '))
vsalario = float(input('Qual o seu salário? '))
ano = float(input('Em quantos anos pretende financia-la? '))
mes = ano*12
pormes = vcasa/mes

#VALIDAÇÃO:
if ano<0 or vsalario<0 or vcasa<0:
    print('Comandos negativos são \033[37;41mINVALIDOS!\033[m ')
    exit()

#EMPRESTIMO:
if pormes>vsalario*0.30:
    print(f'Como a mensalidade {pormes:.2f} é maior que {vsalario*0.30:.2f}, equivalente a 30% do seu salário. O empréstimo foi \033[37;41mNEGADO!\033[m')
else:
    print(f'Como a mensalidade {pormes:.2f} é menor que {vsalario*0.30:.2f}, equivalente a 30% do seu salário. O empréstimo foi \033[37;42mAPROVADO!\033[m.')
