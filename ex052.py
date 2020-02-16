frase = str(input('Digite uma frase (evite acentos): ')).upper().strip().replace(' ', '')
print('\n\033[1;32m{}\033[m ao contrário é \033[1;34m{}\033[m!\n'.format(frase, frase[::-1]))
print('\033[1;36mPALÍNDROMO!\033[m') if frase == frase[::-1] else print('\033[1;31mNÃO É PALÍNDROMO!\033[m')
