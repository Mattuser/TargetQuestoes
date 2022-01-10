import json


with open('dados.json', encoding='utf-8') as my_json:
    date = json.load(my_json)

def menor_valor_ocorrido():
    faturamento_anterior = 0
    menor_faturamento = 0

    for faturamento in date:
        if(faturamento['valor'] < faturamento_anterior):
            menor_faturamento = faturamento['valor']
            faturamento_anterior = menor_faturamento
    return menor_faturamento




def maior_valor_ocorrido():
    faturamento_anterior = 0
    maior_faturamento = 0

    for faturamento in date:
        if(faturamento['valor'] > faturamento_anterior):
            maior_faturamento = faturamento['valor']
            faturamento_anterior = maior_faturamento
    return maior_faturamento


print(f'O menor valor ocorrido em um dia do mês foi: {menor_valor_ocorrido()}')
print(f'O maior valor ocorrido em um dia do mês foi: {maior_valor_ocorrido()}')





