from random import randint
from time import sleep

escolhas = ['Pedra', 'Papel', 'Tesoura']

escolha_pc = randint(1, 3)
escolha_humano = int(input('Escolha sua jogada:\n'
                       '[1]......Pedra\n'
                       '[2]......Papel\n'
                       '[3]......Tesoura\n'
                       '\n--> '))

print('\n\033[1;36mPEDRA! ')
sleep(0.5)
print('PAPEL! ')
sleep(0.5)
print('TESOURA!\033[m\n')
sleep(0.5)

if escolha_pc == escolha_humano:
    print('Empate!')
else:
    if escolha_pc - escolha_humano == 1 or escolha_pc - escolha_humano == -2:
        print('Você perdeu!')
    else:
        print('Você ganhou!')

print('\nVocê jogou {} e o computador jogou {}.'.format(escolhas[escolha_humano - 1], escolhas[escolha_pc - 1]))
