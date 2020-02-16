valor_1 = int(input('Digite um valor inteiro: '))
valor_2 = int(input('Digite outro valor inteiro: '))

if valor_1 == valor_2:
    print('\nNão há valor maior, os dois são iguais.')
else:
    print('\nO primeiro valor é maior ({} > {})'.format(valor_1, valor_2)) \
        if valor_1 > valor_2 \
        else print('O segundo valor é maior ({} > {})'.format(valor_2, valor_1))
