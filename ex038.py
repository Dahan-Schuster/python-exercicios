from datetime import date

ano_nascimento = int(input('Informe seu ano de nascimento, meu jovem: '))
ano_atual = date.today().year

IDADE_ALISTAMENTO = 18

ano_alistamento = ano_nascimento + IDADE_ALISTAMENTO
idade_jovem = ano_atual - ano_nascimento
tempo_para_alistamento = IDADE_ALISTAMENTO - idade_jovem

if idade_jovem < IDADE_ALISTAMENTO:
    print('\n\033[32mVocê ainda vai se alistar!\033[m')
    print('\033[32mFique atento: você deve se alistar em {} anos, no ano {}\033[m'.format(tempo_para_alistamento, ano_alistamento))
elif idade_jovem == IDADE_ALISTAMENTO:
    print('\n\033[33mVocê deve se alistar esse ano! Esteja ligado.\033[m')
    print('\033[33mProcure o órgão responsável na sua cidade.\033[m')
else:
    print('\n\033[31mVocê passo do prazo de alistamento. Se não se alistou, procure o órgão responsável na sua cidade.\033[m')
    print('\033[31mO ano do seu alistamento foi {}, há {} anos.\033[m'.format(ano_alistamento, abs(tempo_para_alistamento)))
