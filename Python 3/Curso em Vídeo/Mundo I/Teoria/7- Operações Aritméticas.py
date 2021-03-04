n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2

print(f'usando {n1} e {n2}, temos que: \n A soma é {s}; \n multiplicação  {m}; \n divisão {d:.3f};', end=' >>>> ')
print(f'divisão inteira {di} e a potência é {e}.')


