print('Solução matemática\n')

numero = int(input('Digite um número entre 1 e 9999: '))
while numero < 1 or numero > 9999:
    numero = int(input('Apenas números entre 1 e 9999: '))

print('{} Unidades'.format(numero%10))
print('{} Dezenas'.format((numero%100)//10))
print('{} Centenas'.format((numero%1000)//100))
print('{} Milhares'.format(numero//1000))

print('\nSolução com string\n')
numero = input('Digite um número entre 1 e 9999: ')
while len(numero) > 4 or numero.count('-') > 0:
    numero = input('Apenas números entre 1 e 9999: ')

numero = '{:0>4}'.format(numero)

print('{} Unidades'.format(numero[3]))
print('{} Dezenas'.format(numero[2]))
print('{} Centenas'.format(numero[1]))
print('{} Milhares'.format(numero[0]))