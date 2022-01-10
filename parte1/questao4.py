
faturamento_por_estado = [
{
        "estado": "SP",
        "valor": 67.836,
        },
    {   
        "estado": "RJ",
        "valor" : 36.678

    },
    {   
        "estado": "MG",
        "valor" : 29.229

    },
    {   
        "estado": "ES",
        "valor" : 27.165

    },
    {   
        "estado": "OUTROS",
        "valor" : 19.849

    },

]

total = 0
percentual = 0
for estado in faturamento_por_estado:
    total += estado['valor']


for estado in faturamento_por_estado:
    nome_estado = estado['estado']
    percentual = (estado['valor'] / total) * 100
    print(f'O valor percentual do estado de {nome_estado} é {percentual}')
    


# O valor percentual do estado de SP é 37.52883705748602
# O valor percentual do estado de RJ é 20.29133034958536
# O valor percentual do estado de MG é 16.170328120072806
# O valor percentual do estado de ES é 15.028463627964616
# O valor percentual do estado de OUTROS é 10.981040844891208