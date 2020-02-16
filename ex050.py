print('''
=============================
    10 TERMOS DE UMA P.A.
=============================''')

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro

for i in range(1, 11):
    print(termo, end=' → ')
    termo += razao
print('FIM')