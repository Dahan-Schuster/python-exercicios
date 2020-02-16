def ler_velocidade():
    return int(input('Qual a velocidade do carro? '))


def calcular_multa():
    return (velocidade - velocidade_maxima) * 7


def multar():
    print('\nVocê foi multado por andar a {} Km/h onde a velocidade máxima permitida é {} Km/h!\nVocê deve pagar R${:.2f}.'.format(velocidade, velocidade_maxima, multa))


velocidade_maxima = 80#km/h

velocidade = ler_velocidade()
multa = calcular_multa()

if velocidade > velocidade_maxima:
    multar()
