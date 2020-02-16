from datetime import date

jovens = 0
adultos = 0
mortos = 0
nao_nascidos = 0

for i in range(1, 8):
    nascimento = int(input('Ano de nascimento da {}º pessoa: '.format(i)))
    idade = date.today().year - nascimento
    if idade >= 18:
        if idade < 110:
            adultos += 1
        else:
            mortos += 1
    else:
        if idade >= 0:
            jovens += 1
        else:
            nao_nascidos += 1

print('\nQuantidade de pessoas que ainda irão nascer: {}'.format(nao_nascidos))
print('Quantidade de jovens: {}'.format(jovens))
print('Quantidade de adultos: {}'.format(adultos))
print('Quantidade de pessoas que estão provavelmente mortas: {}'.format(mortos))