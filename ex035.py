preco_total = float(input('Digite o valor do imóvel. Se necessário, use \033[31mponto\033[m \033[1;32m(R$): '))
salario_mensal = float(
    input('\033[mDigite seu salário mensal. Se necessário, use \033[31mponto\033[m \033[1;32m(R$): '))
numero_de_parcelas = int(input('\033[mDigite a quantidade de anos que quer para pagar o imóvel: '))
while numero_de_parcelas > 60 or numero_de_parcelas < 1:
    numero_de_parcelas = int(input('\033[mApenas valores entre 1 e 60 anos: '))

valor_parcela = preco_total / numero_de_parcelas / 12

porcetagem_valor_parcela = 100 * valor_parcela / salario_mensal

if valor_parcela > salario_mensal * 0.3:
    print(
        "\033[m\n\033[31mDesculpe, " +
        "infelizmente você não está apto a comprar este imóvel com esta quantidade de parcelas.\033[m" +
        "\n\033[31mA parcela custa R${:.2f}, que é {:.2f}% do valor total.\033[m"
        .format(valor_parcela, porcetagem_valor_parcela))

    print(
        '\n\033[1;33m===========================================================\033[m'
        '\n\033[1;33mA prestação deve ser, no máximo, 30% do seu salário mensal.\033[m'
        '\n\033[1;33m===========================================================\033[m')

    novo_valor_parcela = 0;
    pode_pagar = False;
    if (numero_de_parcelas < 60):
        for possivel_novo_numero_de_parcelas in range(numero_de_parcelas, 60):
            novo_valor_parcela = preco_total / possivel_novo_numero_de_parcelas / 12
            if novo_valor_parcela <= salario_mensal * 0.3:
                nova_porcentagem_valor_parcela = 100 * novo_valor_parcela / salario_mensal
                pode_pagar = True;
                break

    print(
        '\033[m\n\033[1;32mMas pode comprar se extender a quantidade de parcelas para {} anos,\033[m\n\033[1;32mficando com uma dívida de mensal de R${:.2f}, {:.2f}% do total.\033[m'.format(
            possivel_novo_numero_de_parcelas, novo_valor_parcela,
            nova_porcentagem_valor_parcela)) if pode_pagar else print(
        '\033[1;31mO sistema não achou nenhuma outra alternativa de parcelamento que esteja dentro do prazo de 60 anos.\033[m')

else:
    print(
        '\033[m\n\033[1;32mVá em frente, você pode comprar este imóvel!\033[m\n\033[1;32mAs parcelas custarão R$ {:.2f} mensais, {:.2f}% do total.\033[m'.format(
            valor_parcela, porcetagem_valor_parcela))
