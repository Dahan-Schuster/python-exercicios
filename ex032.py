numero_1 = int(input('Primeiro número: '))
numero_2 = int(input('Segundo número: '))
numero_3 = int(input('Terceiro número: '))

if numero_1 < numero_2 and numero_3:
    menor = numero_1
elif numero_2 < numero_1 and numero_3:
    menor = numero_2
else:
    menor = numero_3

if numero_1 > numero_2 and numero_3:
    maior = numero_1
elif numero_2 > numero_1 and numero_3:
    maior = numero_2
else:
    maior = numero_3

print('\nMaior: {}\nMenor: {}'.format(maior, menor))

