maior_peso = 0
pessoa_mais_pesada = 0
menor_peso = float("inf")
pessoa_mais_leve = 0

for i in range(1, 6):
    peso = abs(float(input('Peso da {}º pessoa (kg): '.format(i))))
    if peso > maior_peso:
        maior_peso = peso
        pessoa_mais_pesada = i
    if peso < menor_peso:
        menor_peso = peso
        pessoa_mais_leve = i

print('\nA \033[1;34m{}º\033[m pessoa é mais \033[31mpesada\033[m, pesando \033[33m{} kg\033[m'.format(pessoa_mais_pesada, maior_peso))
print('A \033[1;36m{}º\033[m pessoa é mais \033[32mleve\033[m, pesando \033[33m{} kg\033[m'.format(pessoa_mais_leve, menor_peso))