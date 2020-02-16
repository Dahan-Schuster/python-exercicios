nome = input('Informe um nome: ').strip()

print('Todas as letras maiúsculas:', nome.upper())
print('Todas as letras minúsculas:', nome.lower())
print('Quantidade de letras sem espaços:', len(nome.replace(" ", "")))
print('Tamanho do primeiro nome:', len(nome.split()[0]))