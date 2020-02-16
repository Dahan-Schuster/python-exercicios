funcionando = True
salarios_ajustados = []
while(funcionando):
    funcao = input("""
    Qual função deseja utilizar?
                    
    [z]........Conferir ajustes realizados
    [x]........Realizar um ajuste
    [c]........Sair\n\n--> """).upper()

    if funcao == 'Z':
        print('\nFUNCIONÁRIO: SALÁRIO ANTIGO -> NOVO SALÁRIO\n-------------------------------------------')
        if len(salarios_ajustados) > 0:
            for i in range(len(salarios_ajustados)):
                print(salarios_ajustados[i])
        else:
            print('Nenhum salario ajustado ainda.')
    elif funcao == 'X':
        res = 's'
        while res.upper() == 'S':
            funcionario = str(input('\nDigite o nome do funcionário: '))

            novo_salario = 0.0
            salario = float(input('Digite o salário: '))
            if salario > 1250.00:
                novo_salario = salario * 1.1
            else:
                novo_salario = salario * 1.15

            print('\nNovo salário: R${0:.2f}'.format(novo_salario))

            ajuste = "{0}: {1:.2f} -> {2:.2f}".format(funcionario, salario, novo_salario);
            salarios_ajustados.append(ajuste)

            res = input('\nContinuar ajustando? (S/n)')
    elif funcao == 'C':
        funcionando = False
    else:
        print('Escolha inválida. Tente novamente.')

print('Até a próxima!')
