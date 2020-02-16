class Pessoa():
    nome = 'Não informado'
    idade = 'Não informada'
    sexo = 'Desconhecido'

    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo


pessoas = []

total_pessoas = int(input('Quantas pessoas irá cadastrar?: '))

for i in range(0, total_pessoas):
    print('')
    print('*' * 13)
    print('  {}º PESSOA  '.format(i+1))
    print('*' * 13)

    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo: ').upper().strip()[:1]

    pessoa = Pessoa(nome, idade, sexo)
    pessoas.append(pessoa)

soma_das_idades = 0
homem_mais_velho = Pessoa('', 0, '')
quantidade_de_mulheres_menos_de_vinte_anos = 0

for i in range(0, total_pessoas):
    soma_das_idades += pessoas[i].idade

    if pessoas[i].sexo == 'M':
        if pessoas[i].idade > homem_mais_velho.idade:
            homem_mais_velho = pessoas[i]
    else:
        if pessoas[i].idade < 20:
            quantidade_de_mulheres_menos_de_vinte_anos += 1

print('Média de idade do grupo: {:.0f} anos'.format(soma_das_idades / len(pessoas)))
print('O homem mais velho é o {}, com {} anos'.format(homem_mais_velho.nome, homem_mais_velho.idade))
print('Quantidade de mulheres com menos de 20 anos: {}'.format(quantidade_de_mulheres_menos_de_vinte_anos))