from random import randint as pensamento


class ex027():
    jogada_humano = 0
    jogada_maquina = 0
    isAberta = False;

    def __init__(self):
        self.isAberta = True

    def saudar(self):
        print('Pensei em um número de 0 a 5.')

    def pedir_jogada(self):
        try:
            self.jogada_humano = int(input('\nAdvinhe o que estou pensando, humando: '))
        except ValueError:
            print('Apenas números, trouxa!')
            self.pedir_jogada()

    def jogar(self):
        self.jogada_maquina = pensamento(1, 5)


maquina = ex027()
while maquina.isAberta:
    maquina.saudar();
    maquina.jogar()
    maquina.pedir_jogada()

    meus_parabens = 'Uau, você é um ser inferior mas acertou!\nEntretanto, não é grande coisa, visto que as chances eram de 20%.\nNão se vanglorie.';
    estou_decepcionado = 'Era de se esperar... você errou feio.\nPor que ainda tenta?'
    print(meus_parabens) if (maquina.jogada_humano == maquina.jogada_maquina) else print(estou_decepcionado)

    maquina.isAberta = input('Deseja jogar novamente? (S/n)').upper() == 'S';

print('\nFoi uma perda de tempo fútil e angustiante jogar com um humano.\nAté a próxima!')