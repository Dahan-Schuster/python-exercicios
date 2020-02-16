frase = 'Curso em Vídeo Python'

# Fatiamento de string
print('Fatiamento de string\n')
print(frase[9])
print(frase[9:13])
print(frase[9:13:3])
print(frase[:9])
print(frase[9:])
print(frase[9::3])

# Análise de string
print('\nAnálise de string\n')
print('Length:', len(frase))
print('Count \'o\'', frase.count('o'))  # conta a quantidade de letras 'o'
print('Count \'o\'', frase.count('o', 0, 14)) # conta a quantidade de letras 'o' entre os caracteres 0 e 13
print(frase.find('deo')) # encontra o index inicial da primeira ocorrência da string dada. Retorna -1 se não existir
print(frase.find('Android'))
print('Curso' in frase)

# Transformação de string
print('\nTransformação de string\n')
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
frase = '   ' + frase + '    '
print('.'+frase.strip()+'.')    # remove espaços extras no início e no final da string
print('.'+frase.lstrip()+'.')   # remove espaços extras no final da string
print('.'+frase.rstrip()+'.')   # remove espaços extras no início da string
frase = frase.strip()
print(frase.split())
splitedFrase = frase.split()
print(splitedFrase[0])
print(splitedFrase[1][1])
print('-'.join(frase))
print('-'.join(frase.split()))


# Extra
print('\nPrint de um texto grande: três aspas duplas (\"\"\")\n')
print("""A toalha é um dos objetos mais úteis para um mochileiro interestelar. Ela é um item indispensável de sobrevivência, 
porque além de cuidar da higiene, ela pode ser usada para funções distintas, como combate corpo a corpo, 
proteger-se de emanações tóxicas e em situações de emergência para pedir socorro.

Porém o mais importante é o imenso valor psicológico da toalha. Por algum motivo, quando um estrito (isto é, um não-mochileiro) 
descobre que um mochileiro tem uma toalha, ele automaticamente conclui que ele tem também escova de dentes, esponja, sabonete, 
lata de biscoitos, garrafinha de aguardente, bússola, mapa, barbante, repelente, capa de chuva, traje espacial, etc., etc.

Além disso, o estrito terá prazer em emprestar ao mochileiro qualquer um desses objetos, ou muitos outros, que o mochileiro 
por acaso tenha \"acidentalmente perdido\". O que o estrito vai pensar é que, se um sujeito é capaz de rodar por toda a Galáxia, 
acampar, pedir carona, lutar contra terríveis obstáculos, dar a volta por cima e ainda assim saber onde está sua toalha, 
esse sujeito claramente merece respeito.""")
