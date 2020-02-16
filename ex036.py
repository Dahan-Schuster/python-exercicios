from numbers import Number


def binario(decimal):
    numero_binario = ''
    while decimal > 0:
        # uma string armazena cada resto da divisão do número decimal por 2
        numero_binario += str(decimal % 2)

        # o numero decimal é substituido por sua divisão inteira por 2
        decimal = decimal // 2

    # o fatiamento [::-1] simplesmente inverte a string
    # [::-1] pode ser lido como "Do início ao fim da string, retrocedendo sempre uma letra"
    return int(numero_binario[::-1])


def octal(decimal):
    numero_octal = ''
    while decimal > 0:
        numero_octal += str(decimal % 8)
        decimal = decimal // 8

    return int(numero_octal[::-1])


def hexadecimal(decimal):
    # dicionario de letras hexadecimais
    letras_hexa = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    numero_hexadecimal = ''
    while decimal > 0:
        # o método setdefault retorna o equivalente em letra para o resto da divisão
        # e retorna uma string com o próprio resto caso não haja letra
        # Ex1.: resto == 14 -> setdefault(resto, str(resto)) == 'E'
        # Ex2.: resto == 9 -> setdefault(resto, str(resto)) == '9'

        resto = decimal % 16
        numero_hexadecimal += letras_hexa.setdefault(resto, str(resto))
        decimal = decimal // 16

    return numero_hexadecimal[::-1]


continuar = 'S'
while continuar == 'S':

    numero_decimal = int(input('\nDigite um número de base 10 para realizar a conversão: '))
    res = input('Escolha uma das opções de conversão:\n'
                '[1]...........Binário\n'
                '[2]...........Octal\n'
                '[3]...........Hexadecimal\n'
                '\n--> ')

    if res == '1':
        print('{} em base Binária = {}'.format(numero_decimal, binario(numero_decimal)))
        continuar = input('\nDeseja continuar convertendo? (S/n)').upper()
    elif res == '2':
        print('{} em base Octal = {}'.format(numero_decimal, octal(numero_decimal)))
        continuar = input('\nDeseja continuar convertendo? (S/n)').upper()
    elif res == '3':
        print('{} em base Binária = {}'.format(numero_decimal, hexadecimal(numero_decimal)))
        continuar = input('\nDeseja continuar convertendo? (S/n)').upper()
    else:
        print('\033[30;41mVocê digitou algo fora do esperado. Pode tentar novamente?\033[m')
