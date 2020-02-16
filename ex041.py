lado_a = int(input('Digite a medida do primeiro lado: '))
lado_b = int(input('Digite a medida do segundo lado: '))
lado_c = int(input('Digite a medida do terceiro lado: '))

if lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and lado_c < lado_a + lado_b:
    print('\n\033[32mTriângulo válido!\033[m')

    print('O triângulo formado será um \033[33m', end='')
    if lado_a == lado_b == lado_c:
        print('EQUILÁTERO\033[m')
    elif lado_a != lado_b != lado_c != lado_a:
        print('ESCALENO\033[m')
    else:
        print('ISÓSCELES\033[m')


else:
    print('\n\033[31mTriângulo inválido.\033[m')
