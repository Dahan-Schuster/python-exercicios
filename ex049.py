soma = 0
for i in range(1, 7):
    num = int(input('{}º número: '.format(i)))
    if num % 2 == 0:
        soma += num
print('\nSoma dos valores pares = {}'.format(soma))
