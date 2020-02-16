numero = int(input('Digite um número inteiro: '))
cont = 0

print('\nDivisores: (\033[1;33mS\033[m/\033[1;31mn\033[m)', end=' ')
for i in range(1, abs(numero) + 1):
        if numero % i == 0:
            print('\033[1;33m{}\033[m'.format(i), end=' ')
            cont += 1
        else:
            print('\033[31m{}\033[m'.format(i), end=' ')

print('\n\nO número \033[1;34m{}\033[m possui \033[1;34m{}\033[m divisores entre \033[1;34m1\033[m e ele mesmo.'.format(numero, cont))
print('Esse número \033[1;32mÉ\033[m primo.') if cont == 2 else print('Esse número \033[1;31mNÃO\033[m é primo.')
