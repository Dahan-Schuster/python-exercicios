soma = 0
for i in range(0, 501, 3):
    if i % 2 == 1:
        soma += i
print('A \033[1;33msoma\033[m dos \033[1;36mnúmeros ímpares\033[m que são \033[1;33mmúltiplos de três\033[m entre \033[1;33m1\033[m e \033[1;33m500\033[m é igual a \033[1;34m{}\033[m'.format(soma))