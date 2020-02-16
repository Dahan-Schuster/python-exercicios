frase = input('Digite algo: ')

print('Quantidade de letras \'A\':', frase.upper().count('A'))

if frase.upper().count('A') > 0:
    print('Índice da primeira ocorrência:', frase.upper().find('A'))
    print('Índice da última ocorrência:', frase.upper().rfind('A'))
