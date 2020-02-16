distancia = int(input('Digite a distância da sua viagem em Km: '))

if (distancia <= 200):
    preco_por_km = 0.5
    valor_passagem = distancia * preco_por_km
else:
    preco_por_km = 0.45
    valor_passagem = distancia * preco_por_km

print('\nA passagem para uma viagem de {} Km irá custar R${:.2f}.\nPreço por Km: R${:.2f}'.format(distancia, valor_passagem, preco_por_km))